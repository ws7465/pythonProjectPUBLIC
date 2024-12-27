# ###
# Задача "Заморозка кейсов":
# Подготовка:
# В этом задании используйте те же TestCase, что и в предыдущем:
# RunnerTest и TournamentTest.
#
# Часть 1. TestSuit.
#
#     Создайте модуль suite_12_3.py для описания объекта TestSuite.
#     Укажите на него переменной с произвольным названием.
#     Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
#     Создайте объект класса TextTestRunner, с аргументом verbosity=2.
#
# Часть 2. Пропуск тестов.
#
#     Классы RunnerTest дополнить атрибутом is_frozen = False
#       и TournamentTest атрибутом is_frozen = True.
#     Напишите соответствующий декоратор к каждому методу (кроме @classmethod),
#       который при значении is_frozen = False будет выполнять тесты,
#       а is_frozen = True - пропускать и выводить сообщение
#       'Тесты в этом кейсе заморожены'.
#
# Таким образом вы сможете контролировать пропуск всех тестов в TestCase
# изменением всего одного атрибута.
# Запустите TestSuite и проверьте полученные результаты тестов из
# обоих TestCase.
##
###
import unittest
from pprint import pprint
#
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
#
class RunnerTest(unittest.TestCase) :
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        t_walk=Runner('nt_walk')
        for i in range(10) :
            t_walk.walk()
        self.assertEqual(t_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        t_run=Runner('nt_run')
        for i in range(10) :
            t_run.run()
        self.assertEqual(t_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge (self):
        t_walk = Runner('nt_walk')
        t_run=Runner('nt_run')
        for i in range(10) :
            t_walk.walk()
            t_run.run()
        self.assertNotEqual(t_run.distance, t_walk.distance)

##
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers
#
class TournamentTest(unittest.TestCase) :
    is_frozen = True

    @classmethod
    def setUpClass(cls): # в начале, 1 раз
        global all_results
        all_results = {}

    def setUp(self): # перед тестированием, каждый раз
        global pt1
        pt1 = Runner('Усэйн', 10)
        global pt2
        pt2 = Runner('Андрей', 9)
        global pt3
        pt3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls): # после всех тестов, 1 раз
        pass

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_13(self):
        tm_90 = Tournament(90, pt1, pt3)
        all_results = tm_90.start()
        pprint(all_results)
        self.assertTrue(all_results.get(2), 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_23(self):
        tm_90 = Tournament(90, pt2, pt3)
        all_results = tm_90.start()
        pprint(all_results)
        self.assertTrue(all_results.get(2), 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_123(self):
        tm_90 = Tournament(90, pt1, pt2, pt3)
        all_results = tm_90.start()
        pprint(all_results)
        self.assertTrue(all_results.get(3), 'Ник')
###
##
# Пример результата выполнения тестов:
# Вывод на консоль:
# test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
# test_run (tests_12_3.RunnerTest.test_run) ... ok
# test_walk (tests_12_3.RunnerTest.test_walk) ... ok
# test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# ----------------------------------------------------------------------
# Ran 6 tests in 0.000s OK (skipped=3)
# #
# конец задачи
