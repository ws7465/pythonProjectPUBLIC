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
    #print(f'root : {root}')
    #print(f'dirs : {dirs}')
    #print(f'files : {files}')
    for file in files:
        if file == 'module_7_5.py' :
            print(f'dirs : {dirs}')
            filepath = os.path.join('projects Python-PyCharm', 'pythonProject_M7', 'module_7_5.py')
            print(f'filepath : {filepath}')
            filetime = os.path.getmtime('module_7_5.py')
            print(f'filetime : {filetime}')
            formatted_time = time.ctime(filetime)
            print(f'formatted_time : {formatted_time}')
            filesize = os.path.getsize('module_7_5.py')
            print(f'filesize : {filesize}')
            parent_dir = os.path.dirname(filepath)
            print(f'parent_dir : {parent_dir}')
            #formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
          #filesize = ?
          #parent_dir = ?
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:  {formatted_time}, Родительская директория: {parent_dir}')
    else :
        continue
#
# вывод на экран
#
# dirs : ['.git', '.idea', '.venv']
# filepath : projects Python-PyCharm\pythonProject_M7\module_7_5.py
# filetime : 1730542368.113116
# formatted_time : Sat Nov  2 13:12:48 2024
# filesize : 3627
# parent_dir : projects Python-PyCharm\pythonProject_M7
# Обнаружен файл: module_7_5.py, Путь: projects Python-PyCharm\pythonProject_M7\module_7_5.py, Размер: 3627 байт, Время изменения:  Sat Nov  2 13:12:48 2024, Родительская директория: projects Python-PyCharm\pythonProject_M7
#
# ###
#
# Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке проекта (directory = “.”)
# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11,
#
#   конец задания
#
