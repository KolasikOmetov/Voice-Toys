import speech_recognition as sr
keywords = {'Yo-Yo':['yo-yo', 'yo', 'new york', 'ё ё', 'её', 'йо-йо'],
           'ToyPhone':['toy phone', 'iphone', 'телефон', 'фон'],
           'ParrotToy':['parrot', 'parrot toy'],}

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


def main(name):
    print(name)


while True:
    listen()