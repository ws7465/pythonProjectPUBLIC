# #
#       Задача "Записать и запомнить":
#   Создайте функцию custom_write(file_name, strings), которая принимает
#   аргументы file_name - название файла для записи, strings - список строк для записи.
#       Функция должна:
#     - Записывать в файл file_name все строки из списка strings, каждая на новой строке.
#     - Возвращать словарь strings_positions,
#       где ключом будет кортеж (<номер строки>, <байт начала строки>),
#       а значением - записываемая строка.
#       Для получения номера байта начала строки используйте метод tell() перед записью.
#
##
import os
from pprint import pprint
###
def custom_write(file_name, strings) : #
    if not os.path.exists(file_name) :  # если нет файла
        open(file_name, 'a').close()  # создаём
    else :
        open(file_name, 'w').close() # очистим файл
    name = file_name
    fstrings ='' # строки записи в файл
    ns = 0  # № строки
    keys = [] # ключи для strings_positions
    values = [] # значения ключей для strings_positions
    file = open(name, 'a', encoding = 'utf-8')
    for string in strings :
        ns += 1
        ntell = str(file.tell())
        file.write(string + ' \n')
        fstrings += string + ' \n' # что запишется в файл в итоге
        keys.append((ns, ntell)) #
        values.append(string) #
    strings_positions = dict(zip(keys, values))
    file.close()  #
    pprint(fstrings)
    return strings_positions  # словарь из строк файла __file_name.
###
##
#
# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
info = [
     'Text for tell.',
     'Используйте кодировку utf-8.',
     'Because there are 2 languages!',
     'Спасибо!'
     ]
#
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
#
# Вывод на консоль:
## ((1, 0), 'Text for tell.')
## ((2, 16), 'Используйте кодировку utf-8.')
## ((3, 66), 'Because there are 2 languages!')
## ((4, 98), 'Спасибо!')
##
# Вывод на консоль У МЕНЯ ТАК:
# ((1, '0'), 'Text for tell.')
# ((2, '17'), 'Используйте кодировку utf-8.')
# ((3, '68'), 'Because there are 2 languages!')
# ((4, '101'), 'Спасибо!')
# потому-что перед \n стоит пробел (из общих соображений)
#  Как выглядит файл после запуска:
#   ВОТ ТАК
# Text for tell.
# Используйте кодировку utf-8.
# Because there are 2 languages!
# Спасибо!
#
#   конец задачи
#
