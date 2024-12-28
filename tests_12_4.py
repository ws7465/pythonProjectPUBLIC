####
# Задача "Логирование бегунов":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub.
# (Можно скопировать)
# Основное обновление - выбрасывание исключений, если передан неверный тип в name
# и если передано отрицательное значение в speed.
#
# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig
# на следующие параметры:
#
#     Уровень - INFO
#     Режим - запись с заменой('w')
#     Название файла - runner_tests.log
#     Кодировка - UTF-8
#     Формат вывода - на своё усмотрение, обязательная информация:
#           уровень логирования, сообщение логирования.
#
#
# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
#
#     Оберните основной код конструкцией try-except.
#     При создании объекта Runner передавайте отрицательное значение в speed.
#     В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
#     В блоке except обработайте исключение соответствующего типа и логируйте
#     его на уровне WARNING с сообщением "Неверная скорость для Runner".
#
# test_run:
#
#     Оберните основной код конструкцией try-except.
#     При создании объекта Runner передавайте что-то кроме строки в name.
#     В блок try добавьте логирование INFO с сообщением 'test_run" выполнен успешно'
#     В блоке except обработайте исключение соответствующего типа и логируйте его
#     на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
#
##
###
import unittest
import logging

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано '
                            f'{type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

##
class RunnerTest(unittest.TestCase) :

    def test_walk(self):
        try:
            #first = Runner('Вася', -10)
            first = Runner('Вася', 10)
            for i in range(10) :
                first.walk()
            self.assertEqual(first.distance, 100)
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.warning(f'Неверная скорость для Runner')

    def test_run(self):
        try:
            #second=Runner(12345, 5)
            second = Runner('Илья', 5)
            for i in range(10) :
                second.run()
            self.assertEqual(second.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f'Неверный тип данных для объекта Runner')

##
if __name__ == "tests_12_4":
    logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8',
            filename='tests.log', format='%(asctime)s | %(levelname)s | %(message)s')
#
##
###
##
# Пример результата выполнения программы:
# Пример полученного файла логов runner_tests.log:
# 2024-12-28 08:24:18,223 | WARNING | Неверный тип данных для объекта Runner
# 2024-12-28 08:24:18,224 | WARNING | Неверная скорость для Runner
# 2024-12-28 08:38:45,899 | INFO | "test_run" выполнен успешно
# 2024-12-28 08:38:45,899 | INFO | "test_walk" выполнен успешно
# #
# #
# конец задачи
#
