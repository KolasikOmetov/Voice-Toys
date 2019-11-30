import speech_recognition as sr
import os
import TTS


keywords = {'Yo_Yo':['yo-yo', 'yo', 'new york', 'ё ё', 'её', 'йо-йо'],
           'ToyPhone':['toy phone', 'iphone', 'телефон', 'фон'],
           'ParrotToy':['parrot', 'parrot toy'],}

path_directory= os.path.dirname(os.path.realpath(__file__))
ParrotToy_path = path_directory + '\ParrotToy_0.1\ParrotToy.py'
ToyPhone_path = path_directory + '\Toyphone_0.2\TOYPHONE.py'
Yo_Yo_path = path_directory + 'Yo-Yo_0.5.py'

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ru-RU')
        print("Вы сказали: " + query.lower())
        for name in keywords:
            for keyword in keywords[name]:
                if keyword in query:
                   main(name)
    except sr.UnknownValueError: # если есть ошибки
        pass
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


def ParrotToy():
    TTS.talk('Запущен ParrotToy')
    os.system(ParrotToy_path)

def ToyPhone():
    print('Запущен ToyPhone')
    os.system(ToyPhone_path)

def Yo_Yo():
    TTS.talk('Запущена Yo-Yo')
    os.system(Yo_Yo_path)

def main(name):
    exec(name+"()")

main('её')

# while True:
#     listen()