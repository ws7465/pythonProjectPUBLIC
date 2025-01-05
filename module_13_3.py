###
# Python 3.9.13 ;  aiogram 2.25.1
#
# requirements.txt
#
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
#
# ###
# Задача "Он мне ответил!":
# Измените функции start и all_messages так, чтобы вместо вывода в консоль
# строки отправлялись в чате телеграм.
# Запустите ваш Telegram-бот и проверьте его на работоспособность.
#
# Пример результата выполнения программы:
#
# привет!
# введите команду /start чтобы начать общение.
# /start
# привет! я бот помогающий твоему здоровью.
#
#Updates were skipped successfully.
#Goodbye!
#
# Примечания:
#
#     Для ответа на сообщение запускайте метод answer асинхронно.
#     При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!

# #
from aiogram.contrib.fsm_storage.memory import MemoryStorage # для v 2.25
from aiogram import Bot, Dispatcher, executor, types # для v 2.25
import asyncio
#
api = '33333333333333333333333333333333333333'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
#
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
#
@dp.message_handler()
async def start(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
#
if __name__ == '__main__' :
    executor.start_polling(dp, skip_updates = True) # для v 2.25
#
##
