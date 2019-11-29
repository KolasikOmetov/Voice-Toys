import speech_recognition as sr # это та библа с которой работаем
# таким образом мы её подключили как sr

def listen():
    # присваиваем объект распознования
    r = sr.Recognizer()
    # спрашиваем микрофон у системы и говорим что он называется source
    with sr.Microphone(device_index=1) as source:
        # Просто вывод, чтобы мы знали когда говорить
        print("Говорите")
        # используем adjust_for_ambient_noise для удаления
        # посторонних шумов из аудио дорожки
        r.adjust_for_ambient_noise(source, duration=1)
        # Полученные данные записываем в переменную audio
        # пока мы получили лишь mp3 звук
        audio = r.listen(source)
    try: #пробуем выполнить код если он без ошибок
        # отправляем аудиоречь в гугл распознователь
        query = r.recognize_google(audio, language='ru-RU')
        print("Вы сказали: " + query.lower())
    except sr.UnknownValueError: # если есть ошибки
       print("Речь не распознана")
       # запускаем функцию прослушивания и распознание занаво
       query = ""
    return query.lower()# Возвращаем строку с нашим сказаным текстом
# .lower() сделать текст в нижнем регистре