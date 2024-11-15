###
#       Задача "Range - это просто":
#   Создайте пользовательский класс исключения StepValueError,
#       который наследуется от ValueError.
#   Наследования достаточно, класс оставьте пустым при помощи оператора pass.
#
# Создайте класс Iterator, который обладает следующими свойствами:
# Атрибуты объекта:
#
#     start - целое число, с которого начинается итерация.
#     stop - целое число, на котором заканчивается итерация.
#     step - шаг, с которым совершается итерация.
#     pointer - указывает на текущее число в итерации (изначально start)
#
# Методы:
#
#     __init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага. В этом методе в первую очередь проверяется step на равенство 0. Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')
#     __iter__ - метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
#     __next__ - метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута step итерация завершится либо когда pointer станет больше stop, либо меньше stop. Учтите это при описании метода.
#
#
# Пункты задачи:
#
#     Создайте класс исключения StepValueError.
#     Создайте класс Iterator и опишите его атрибуты и методы.
#     Создайте несколько объектов класса Iterator и совершите итерации с ними при помощи цикла for.
#
###
class Iterator : #
    def __init__(self, start, stop, step = 1) :
        if step == 0 :  raise StepValueError('шаг не может быть равен 0')
        self.start = int(start)
        self.stop = int(stop)
        self.step = int(step)
#
    def __iter__(self) :
        self.pointer = self.start
        return self
#
    def __next__(self) :
        s = self.pointer
        if self.step > 0 and self.pointer > self.stop :  raise StopIteration()
        if self.step < 0 and self.pointer < self.stop :  raise StopIteration()
        self.pointer += self.step
        return s
#
class StepValueError(ValueError) : #
    pass
##
#
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
#
try:
    iter2 = Iterator( -5, 1)
    for i in iter2:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
print()
#
try:
    iter3 = Iterator( 6, 15, 2)
    for i in iter3:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
print()
#
try:
    iter4 = Iterator( 5, 1, -1)
    for i in iter4:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
print()
#
try:
    iter5 = Iterator( 10, 1)
    for i in iter5:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
#
##
###
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# try:
# iter1 = Iterator(100, 200, 0)
# for i in iter1:
# print(i, end=' ')
# except StepValueError:
# print('Шаг указан неверно')
#
# iter2 = Iterator(-5, 1)
# iter3 = Iterator(6, 15, 2)
# iter4 = Iterator(5, 1, -1)
# iter5 = Iterator(10, 1)
#
#
# for i in iter2:
# print(i, end=' ')
# print()
# for i in iter3:
# print(i, end=' ')
# print()
# for i in iter4:
# print(i, end=' ')
# print()
# for i in iter5:
# print(i, end=' ')
# print()
#
# Вывод на консоль:
# Шаг указан неверно
# -5 -4 -3 -2 -1 0 1
# 6 8 10 12 14
# 5 4 3 2 1
#
#           Примечания:
#     Особое внимание уделите методу __next__ и условиям в нём.
###
# #
# # конец задачи
# #
