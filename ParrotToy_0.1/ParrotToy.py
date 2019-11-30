import time
import STT
import TTS

# по номеру получаем текстовую запись дня недели
def setDayWeek():
    days = {
    '1': "Понедельник",
    '2': "Вторник",
    '3': "Среда",
    '4': "Четверг",
    '5': "Пятница",
    '6': "Суббота",
    '7': "Воскресенье"}

    day = time.strftime("%w")
    return days[day]

def setMonth():
    Months = {
    'Jan': "Январь",
    'Feb': "Февраль",
    'Mar': "Март",
    'Apr': "Апрель",
    'May': "Май",
    'Jun': "Июнь",
    'Jul': "Июль",
    'Aug': "Август",
    'Sep': "Сентябрь",
    'Oct': "Октябрь",
    'Nov': "Ноябрь",
    'Dec': "Декабрь",
    }

    month = time.strftime("%b")
    return Months[month]

# получаем дату
def getDate():
    return time.strftime("%H:%M ")+setDayWeek()+", "+setMonth()+time.strftime("%e, %Y")

# получаем только время
def getTime():
    return time.strftime("%H:%M:%S")+' '

# получаем дату как строку для названия
def getDateName():
    return time.strftime("%e_%B_%Y_%H-%M-%S")


def main():
    file_name = getDateName()+'.txt'
    with open(file_name, 'w', encoding='utf-8') as f:
        TTS.talk('Запись началась')
        f.write(getDate())
        record(f)


def record(file):
    stop = 1 # означает что запись может быть запущена
    while stop: # проверка допустимости записи
        file.write('\n'+getTime())  # запись текущего времени
        text = STT.listen()
        if 'стоп' in text:
            stop = 0 # запрет на дальнейшее распознование записи
            file.write("Конец записи")
            TTS.talk("Конец записи")
        # elif ' пауза' in text:
        #     f.write("Запись на паузе")
        #     break
        else:
            file.write(text)

main()