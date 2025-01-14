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
# Задача "Ещё больше выбора":
# Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку
# 'Рассчитать' присылалась Inline-клавиатруа.
# Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
#
#     С текстом 'Рассчитать норму калорий' и callback_data='calories'
#     С текстом 'Формулы расчёта' и callback_data='formulas'
#
# Создайте новую функцию main_menu(message), которая:
#
#     Будет обёрнута в декоратор message_handler, срабатывающий при передаче
#     текста 'Рассчитать'.
#     Сама функция будет присылать ранее созданное Inline меню и текст
#     'Выберите опцию:'
#
# Создайте новую функцию get_formulas(call), которая:
#
#     Будет обёрнута в декоратор callback_query_handler, который будет реагировать
#     на текст 'formulas'.
#     Будет присылать сообщение с формулой Миффлина-Сан Жеора.
#
# Измените функцию set_age и декоратор для неё:
#
#     Декоратор смените на callback_query_handler, который будет реагировать
#     на текст 'calories'.
#     Теперь функция принимает не message, а call.
#     Доступ к сообщению будет следующим - call.message.
#
# По итогу получится следующий алгоритм:
#
#     Вводится команда /start
#     На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
#     В ответ на кнопку 'Рассчитать' присылается Inline меню:
#       'Рассчитать норму калорий' и 'Формулы расчёта'
#     По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
#     По Inline кнопке 'Рассчитать норму калорий' начинает работать машина
#     состояний по цепочке.
#
###
#import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
 #
api = '6666666666666666666666666666666666666666'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
#
kbr = ReplyKeyboardMarkup(resize_keyboard=True)
but1 = KeyboardButton(text='Рассчитать') #
but2 = KeyboardButton(text='Информация') #
kbr.row(but1, but2) # горизонтальная клава с 2-мя кнопками
#
kbl = InlineKeyboardMarkup(resize_keyboard=True) # создать клавиатуру и авторазмер
but3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
but4 = InlineKeyboardButton(text='формула расчёта', callback_data='formulas')
kbl.row(but3, but4) #
#
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kbr)
#
@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kbl)
#
@dp.callback_query_handler(text='formulas') # обработчик кнопки but4
async def get_formulas(call):
    await call.message.answer('вес(кг)*10)+(рост(см)*6.25)-(возраст(лет)*5)+5')
    await call.answer()
#
@dp.callback_query_handler(text=['calories']) # обработчик кнопки but3
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await UserState.age.set()
#
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()
#
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()
#
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    сalories = (int(data['weight']) * 10) + (int(data['growth']) * 6.25) - (int(data['age']) * 5) + 5
    await message.answer(f"Ваша норма калорий : {сalories}")

    await state.finish()
#
@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
##
if __name__ == '__main__' :
    executor.start_polling(dp, skip_updates = True) # для v 2.25

###
#
# Пример результата выполнения программы:
#
# привет !
# Введите команду /start, чтобы начать общение.
# /start
# привет! я бот помогающий твоему здоровью.
# РАССЧИТАТЬ     ИНФОРМАЦИЯ
#
# После нажатия на кнопку 'Рассчитать':
#
# 'Рассчитать норму калорий' 'Формулы расчёта'
#
#'Рассчитать норму калорий'
# Введите свой возраст:
# 24
# Введите свой рост:
# 178
# Введите свой вес:
# 110
# Ваша норма калорий 2097.50
#
# 'Формула расчёта'
# (вес(кг)*10)+(рост(см)*6.25)-(возраст(лет)*5)+5
# #
# #Updates were skipped successfully.
# #Goodbye!
#
# Примечания:
#
#     При отправке вашего кода на GitHub не забудьте убрать ключ для подключения
#     к вашему боту!
#
####
