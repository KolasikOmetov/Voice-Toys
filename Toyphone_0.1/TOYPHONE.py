import keyboard
import time
import STT
import sys

def delete_word(word, sentence):
    index_begin = sentence.find(word)
    sentence = sentence[:index_begin] + sentence[index_begin + len(word):]
    return sentence


def SearchInCatalog(catalog, query, command):
    for construction in catalog:
        for variant in catalog[construction]:
            if variant in query:
                command = command + "+" + construction
                query = delete_word(variant, query)
    return query, command


possible_words = {
    'stop': ['стоп', 'хватит', 'замолчи', 'заткнись'],
    'ctrl': ['контроль', 'control', 'ctrl'],
    'shift': ['shift', 'шифт'],
    'space': ['space', 'пробел'],
    'f5': ['f5', 'ф5'],
    'enter': ['enter', 'энтер'],
    83: ['вверх'],
    84: ['вниз'],
    79: ['влево', 'налево'],
    89: ['вправо', 'направо'],
    'shift+=': ['плюс', '+'],
    '1': ['1', 'один', 'первый', 'первая', 'первое'],
    '2': ['2', 'два', 'второй', 'вторая', 'второе'],
    'a': ['a'],
    'b': ['b'],
    'c': ['c'],
    'd': ['d'],
    'e': ['e'],
    'f': ['f'],
    'g': ['g'],
    'h': ['h'],
    'i': ['i'],
    'j': ['j'],
    'k': ['k'],
    'l': ['l'],
    'm': ['m'],
    'n': ['n'],
    'o': ['o'],
    'p': ['p'],
    'q': ['q'],
    'r': ['r'],
    's': ['s'],
    't': ['t'],
    'u': ['u'],
    'v': ['v'],
    'w': ['w'],
    'x': ['x'],
    'y': ['y'],
    'z': ['z'],
}

# possible_words_EN = {
#     'stop': ['stop'],
#     'ctrl': ['control', 'ctrl'],
#     'shift': ['shift'],
#     '\+': ['plus', '+'],
#     'a': ['a'],
#     'b': ['b'],
#     'c': ['c'],
#     'd': ['d'],
#     'e': ['e'],
#     'f': ['f'],
#     'g': ['g'],
#     'h': ['h'],
#     'i': ['i'],
#     'j': ['j'],
#     'k': ['k'],
#     'l': ['l'],
#     'm': ['m'],
#     'n': ['n'],
#     'o': ['o'],
#     'p': ['p'],
#     'q': ['q'],
#     'r': ['r'],
#     's': ['s'],
#     't': ['t'],
#     'u': ['u'],
#     'v': ['v'],
#     'w': ['w'],
#     'x': ['x'],
#     'y': ['y'],
#     'z': ['z'],
# }




def Translate_Commands(query):
    command = ""
    query, command = SearchInCatalog(possible_words, query.lower(), command)

    if command == '':
        print("Не удалось распознать команду")
        return ""
    elif 'stop' in command:
        print("Программа завершена")
        sys.exit(0)
    else:
        print(command[1:])
        time.sleep(2)
        keyboard.press_and_release(command[1:])

# while True:
#     Translate_Commands(STT.listen())
Translate_Commands('плюс')