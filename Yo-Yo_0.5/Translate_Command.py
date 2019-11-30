import sys
import executeProgram as ep

def delete_word(word, sentence):
    index_begin = sentence.find(word)
    sentence = sentence[:index_begin] + sentence[index_begin + len(word):]
    return sentence


def take_arguments(command):
    exec('ep.nameFunc = ep.' + command)
    return ep.nameFunc


def change_word(bad_word, sentence, good_word):
    index_begin = sentence.find(bad_word)
    sentence = sentence[:index_begin] + "'" + good_word + "'" + sentence[index_begin + len(bad_word):]
    return sentence

def change_word2(bad_word, sentence, good_word):
    print(sentence)
    index_begin = sentence.find(bad_word)
    sentence = sentence[:index_begin] + "" + good_word + "" + sentence[index_begin + len(bad_word):]
    print(sentence)
    return sentence


def SearchInCatalog(catalog, query, command):
    for construction in catalog:
        for variant in catalog[construction]:
            if variant in query:
                command = command + construction
                query = delete_word(variant, query)
                return query, command
    return query, command


def ChangeInArguments(query, arguments):
    query_words = query.split()
    if arguments == '':
        return query, arguments
    mas_of_arguments = arguments.split(", ")
    for num_word in range(len(mas_of_arguments)):
        try:
            arguments = change_word(mas_of_arguments[num_word], arguments, query_words[num_word])
            query = delete_word(query_words[num_word], query)
        except:
            arguments = change_word(mas_of_arguments[num_word], arguments, mas_of_arguments[num_word])
    return query, arguments


possible_words = {
    'ParrotToy': ['запиши текст', 'записывай текст', 'пиши текст', 'включи диктофон', 'включи parrot toy'],
    'Toyphone': ['управлять клавиатурой', 'управлять клавиатурой голосом', 'управлять клавиатурой с помощью голоса',
                 'управляю клавиатурой', 'управлять клавиатурой голосом', 'управлять клавиатурой с помощью голоса',],
}






def Translate_Commands(query):
    command = ""

    query, command = SearchInCatalog(possible_words, query, command)

    if command == '':
        print("Не удалось распознать команду")
        return ""
    elif command == 'stop':
        print("Программа завершена")
        sys.exit(0)
    print('so: ' + command)
    try:
        arguments = ep._get_signature(take_arguments(command))
        arguments = arguments[1:len(arguments) - 1]
        query, arguments = ChangeInArguments(query, arguments)

        command += "("
        command += arguments
        command += ")"
    except:
        command = "Not exist"

    return command

print(Translate_Commands("запиши текст"))
#print(Translate_Commands('хватит'))
#print(Translate_Commands("диктую"))
# input().lower()