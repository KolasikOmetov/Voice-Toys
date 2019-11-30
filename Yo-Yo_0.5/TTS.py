import win32com.client as wincl

# Функция, позволяющая проговаривать слова
# Принимает параметр "Слова" и прогроваривает их
def talk(words):
    print(words)
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Rate = 1
    speak.Voice = speak.GetVoices().Item(0)
    speak.Speak(words)
