##
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
# 1.	Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# 2.	Примените os.path.join для формирования полного пути к файлам.
# 3.	Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# 4.	Используйте os.path.getsize для получения размера файла.
# 5.	Используйте os.path.dirname для получения родительской директории файла.
#
# Комментарии к заданию:
#
# Ключевая идея – использование вложенного for
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
#
###
import os
import time
import re
from pprint import pprint
#
directory = '.'
for root, dirs, files in os.walk(directory):
    print(f'root : {root}')
    print(f'dirs : {dirs}')
    print(f'files : {files}')
    for dir in dirs :
        for file in files:
                filepath = os.path.join(root, dir)
                filetime = os.path.getmtime(filepath)
                formatted_time = time.ctime(filetime)
                filesize = os.path.getsize(filepath)
                parent_dir = os.path.dirname(filepath)
                pprint(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:  {formatted_time}, Родительская директория: {parent_dir}')
# ###
#
# Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке проекта (directory = “.”)
# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11,
#
#   конец задания
#
