import speech_recognition as sr
from threading import Thread, RLock


class Microfone:
    texto = []

    @classmethod
    def listen_micro(cls):
        micro = sr.Recognizer()  # habilita micro
        n = 0
        with sr.Microphone() as code:  # usa o micro
            print("Precione ctrl c para sair")
            while n < 10:
                micro.adjust_for_ambient_noise(code)  # tira ruido
                print("PARLA!")
                audio = micro.listen(code)
                try:
                    phrase = micro.recognize_google(audio, language='pt-BR')
                    Microfone.texto.append(str(phrase) + " ")
                    print(f"YOU SAY: {phrase}")
                    n += 1
                except sr.UnknownValueError:
                    print("Não compreendi")


    @classmethod
    def write(cls):
        with open("youSaid.txt", 'a') as f:
            for itens in Microfone.texto:
                f.writelines(itens + '\n')
            #f.write()


if __name__ == '__main__':
    with RLock():
        th = Thread(target=Microfone.listen_micro, args=())
        th1 = Thread(target=Microfone.write, args=())
        th.start()
        th.join()
        th1.start()
        th1.join()
