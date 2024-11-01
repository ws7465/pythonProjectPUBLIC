##
#
#       Задача "Найдёт везде":
#   Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
#        Объект этого класса должен принимать при создании неограниченного количество
#   названий файлов и записывать их в атрибут file_names в виде списка или кортежа.
#
#       Также объект класса WordsFinder должен обладать следующими методами:
#   get_all_words - подготовительный метод, который возвращает словарь следующего вида:
#       {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'],
#       'file3.txt': ['word5', 'word6', 'word7']}
# Где:
##     'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
#     ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7']
#                                       - слова содержащиеся в этом файле.
##          Алгоритм получения словаря такого вида в методе get_all_words:
##    - Создайте пустой словарь all_words.
#     - Переберите названия файлов и открывайте каждый из них, используя оператор with.
#     - Для каждого файла считывайте единые строки, переводя их в нижний регистр
#          (метод lower()).
#     - Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
#          (тире обособлено пробелами, это не дефис в слове).
#     -  Разбейте эту строку на элементы списка методом split().
#          (разбивается по умолчанию по пробелу)
#     - В словарь all_words запишите полученные данные,
#          ключ - название файла, значение - список из слов этого файла.
#
#
#   find(self, word) - метод, где word - искомое слово.
#        Возвращает словарь, где ключ - название файла,
#           значение - позиция первого такого слова в списке слов этого файла.
#   count(self, word) - метод, где word - искомое слово. Возвращает словарь,
#       где ключ - название файла, значение - количество слова word в списке слов
#       этого файла.
#   В методах find и count пользуйтесь ранее написанным методом get_all_words
#   для получения названия файла и списка его слов.
#   Для удобного перебора одновременно ключа(названия) и значения(списка слов)
#   можно воспользоваться методом словаря - item().
#
# for name, words in get_all_words().items():
#   # это Логика методов find или count
#
##
###
#
import os
import re
from pprint import pprint
###
#
class WordsFinder : #
    file_names = [] #
#
    def __init__(self, *args) : #
        for i in args : #
            self.i = i
            WordsFinder.file_names.append(i) #
        self.file_names = WordsFinder.file_names #
        #print(args)
        #pprint(locals())
        #pprint(globals())
        #pprint(WordsFinder.file_names)
        #pprint(self.file_names)
#
    def get_all_words(self) : # возвращает словарь
        all_words = {}  # вида:  {'file1.txt': ['word1', 'word2'], ... }
        keys = []
        values = []
        for file_name in self.file_names :
            keys.append(file_name)
            value = []
            if not os.path.exists(file_name) :  # если нет файла
                open(file_name, 'a').close()  # создаём
            with open(file_name, encoding = 'utf-8') as file : #
                for line in file : #
                    #print(f'line : {line}')
                    line = line.lower()
                    line = re.sub(r' - ', '', line)
                    line = re.sub(r'[,.=!?;:]', '', line)
                    value.append(line.split())
            values.append(value)
        all_words = dict(zip(keys, values))
        return all_words
#
    def find(self, word) : # где word - искомое слово.
        key = []
        val = []
        word = word.lower()
        all_words = self.get_all_words() #
        for f_name in self.file_names :
            for file_name, words in all_words.items() : #
                key.append(file_name)
                ind = ''
                for li in words:  #
                    if word in li:
                        ind = li.index(word) + 1
                        break
                    isli = isinstance(li, list)
                    if (isli == True) :
                        for l in li :
                            if word in l :
                                ind = l.index(word) + 1
                                break
                val.append(ind)
        # print(f' key:  {key}')
        # print(f' val:  {val}')
        return dict(zip(key, val)) # в списке слов этого файла.
#
    def count(self, word) : #
            key = []
            val = []
            word = word.lower()
            all_words = self.get_all_words() #
            for f_name in self.file_names :
                for file_name, words in all_words.items() : #
                    key.append(file_name)
                    cou = 0
                    for li in words:  #
                        if word in li:
                            cou += li.count(word)
                    val.append(cou)
            # print(f' key:  {key}')
            # print(f' val:  {val}')
            return dict(zip(key, val)) # в списке слов этого файла.
#
###
##
#
#   Пример выполнения программы:
#  Представим, что файл 'test_file.txt' содержит следующий текст:
#
# It's a text for task Найти везде,
# Используйте его для самопроверки.
# Успехов в решении задачи!
# text text text
#
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
#
# Вывод на консоль:
#
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде',
#   'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении',
#   'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}
#
# Запустите этот код с другими примерами предложенными здесь
#(https://drive.google.com/drive/folders/1IJEynqs2lk-uP1wrVBpm_w3qnEQCCx6O?usp=sharing)
# Если решение верное, то результаты должны совпадать с предложенными.
#
#       Примечания:
#
#     - Регистром слов при поиске можно пренебречь. ('teXT' ~ 'text')
#     - Решайте задачу последовательно - написав один метод,
#       проверьте результаты его работы.
#
#
#  конец задания
#
