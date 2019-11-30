import sys
import executeProgram as ep
import Translate_Command as TC
import TTS
import STT


#Глобальные переменные
text = '' # хранение текста


def main(s):
        command = TC.Translate_Commands(s)
        print(command)
        if command == '':
            pass
        elif command[len(command)-1] == ')':
            exec('global text\ntext = ep.' + command)
            text()
        else:
            TTS.talk('Нет такой команды')



TTS.talk('ё ё запущена. Я вас слушаю')
main(STT.listen())