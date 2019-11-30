import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        # Просто вывод, чтобы мы знали когда говорить
        print("Говорите")
        # Устанавливаем паузу, чтобы прослушивание
        # началось лишь по прошествию 1 секунды
        r.pause_threshold = 1
        # используем adjust_for_ambient_noise для удаления
        # посторонних шумов из аудио дорожки
        r.adjust_for_ambient_noise(source, duration=1)
        # Полученные данные записываем в переменную audio
        # пока мы получили лишь mp3 звук
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ru-RU')
        print("Вы сказали: " + query.lower())
    except sr.UnknownValueError:
       print("Речь не распознана")
       query = listen()
    return query.lower()
