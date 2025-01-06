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
# Задача "Меньше текста, больше кликов":
# Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела
# для расчёта калорий выдавались по нажатию кнопки.
#
#     Измените massage_handler для функции set_age. Теперь этот хэндлер будет
#     реагировать на текст 'Рассчитать', а не на 'Calories'.
#     Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней
#     со следующим текстом: 'Рассчитать' и 'Информация'. Сделайте так,
#     чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи
#     параметра resize_keyboard.
#     Используйте ранее созданную клавиатуру в ответе функции start,
#     используя параметр reply_markup.
#
# В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками.
# При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age
# с которой начинается работа машины состояний для age, growth и weight.
###
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
 #
api = '555555555555555555555555555555555555555555555'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
#
kb = ReplyKeyboardMarkup(resize_keyboard=True) # создать клавиатуру # автоподстройка под размер
but1 = KeyboardButton(text='Рассчитать') # кнопка 1
but2 = KeyboardButton(text='Информация') # кнопка 2
kb.row(but1, but2) # горизонтальная клава с 2-мя кнопками
#
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)
    # новый параметр - вывод клавиатуры reply_markup=kb
#
@dp.message_handler(text=['Рассчитать']) # обработчик кнопки but1 'Рассчитать'
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
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
    #await message.answer(f"возраст: {data['age']}\n"
    #                     f"рост: {data['growth']}\n"
    #                     f"вес: {data['weight']}")
    await state.finish()
#
@dp.message_handler()
async def start(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
##
if __name__ == '__main__' :
    executor.start_polling(dp, skip_updates = True) # для v 2.25
###
#
# Пример результата выполнения программы:
#
# Клавиатура по команде /start:
#
# привет !
# Введите команду /start, чтобы начать общение.
# /start
# привет! я бот помогающий твоему здоровью.
# РАССЧИТАТЬ     ИНФОРМАЦИЯ
#
# После нажатия на кнопку 'Рассчитать':
#
# Введите свой возраст:
# 24
# Введите свой рост:
# 178
# Введите свой вес:
# 110
# Ваша норма калорий 2097.50
#
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
