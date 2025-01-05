###
# Python 3.9.13 ;  aiogram 2.25.1
# requirements.txt

# aiogram==2.25.1
# aiohttp==3.8.6
# aiosignal==1.3.1
# async-timeout==4.0.3
# attrs==23.2.0
# Babel==2.9.1
# certifi==2024.7.4
# charset-normalizer==3.3.2
# frozenlist==1.4.1
# idna==3.7
# magic-filter==1.0.12
# multidict==6.0.5
# pytz==2024.1
# yarl==1.9.4

# ###
# Подготовка:
# Выполните все действия представленные в предыдущих видео модуля,
# создав и подготовив Telegram-бот для дальнейших заданий.
# Нужные версии для 13 и 14 модулей и вашего виртуального окружения находятся здесь.
# не помните, как установить необходимые библиотеки, обратитесь к материалам 11 модуля.
# Актуальная версия Python для дальнейшей работы - 3.9.13.
#
# Задача "Бот поддержки (Начало)":
# К коду из подготовительного видео напишите две асинхронные функции:
#
#     start(message) - печатает строку в консоли
#                   'Привет! Я бот помогающий твоему здоровью.' .
#                   Запускается только когда написана команда '/start' в чате с ботом.
#                   (используйте соответствующий декоратор)
#     all_massages(message) - печатает строку в консоли
#                   'Введите команду /start, чтобы начать общение.'.
#                   Запускается при любом обращении не описанном ранее.
#                   (используйте соответствующий декоратор)
#
#   Запустите ваш Telegram-бот и проверьте его на работоспособность.
#   Пример результата выполнения программы:
#   Ввод в чат Telegram:
# Хэй!
# /start
#   Вывод в консоль:
# Updates were skipped successfully.
# Введите команду /start, чтобы начать общение.
# Привет! Я бот помогающий твоему здоровью.
#
# Примечания:
#
#     Для ответа на сообщение используйте декоратор message_handler.
#     При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!
# #
# #
from aiogram.contrib.fsm_storage.memory import MemoryStorage # для v 2.25
from aiogram import Bot, Dispatcher, executor, types # для v 2.25
import asyncio
#
api = '999999999999999999999999999'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
#
@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
#
@dp.message_handler()
async def start(message):
    print('Введите команду /start, чтобы начать общение.')
#
if __name__ == '__main__' :
    executor.start_polling(dp, skip_updates = True) # для v 2.25
#
##

#Updates were skipped successfully.
#Введите команду /start, чтобы начать общение.
#Привет! Я бот помогающий твоему здоровью.
#Goodbye!
