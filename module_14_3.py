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
# Задача "Витамины для всех!":
# Подготовка:
# Подготовьте Telegram-бота из последнего домашнего задания 13 модуля сохранив
# код с ним в файл module_14_3.py.
# Если вы не решали новые задания из предыдущего модуля рекомендуется выполнить их.
#
# Дополните ранее написанный код для Telegram-бота:
# Создайте и дополните клавиатуры:
#
#     В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
#     Создайте Inline меню из 4 кнопок с надписями
#     "Product1", "Product2", "Product3", "Product4".
#     У всех кнопок назначьте callback_data="product_buying"
#
# Создайте хэндлеры и функции к ним:
#
#     Message хэндлер, который реагирует на текст "Купить" и оборачивает
#       функцию get_buying_list(message).
#     Функция get_buying_list должна выводить надписи 'Название:
#     Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза.
#       После каждой надписи выводите картинки к продуктам.
#       В конце выведите ранее созданное Inline меню с надписью
#       "Выберите продукт для покупки:".
#     Callback хэндлер, который реагирует на текст "product_buying"
#       и оборачивает функцию send_confirm_message(call).
#     Функция send_confirm_message, присылает сообщение
#       "Вы успешно приобрели продукт!"
# #
###
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
 #
api = '3333333333333333333333333333333333333333333'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
#
kbr = ReplyKeyboardMarkup (
    keyboard= [
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [
            KeyboardButton(text='Купить')
        ]
    ], resize_keyboard=True
)

#
catalog_kb = InlineKeyboardMarkup (
    inline_keyboard= [
        [InlineKeyboardButton(text='Product1', callback_data='product_buying'),
        InlineKeyboardButton(text='Product2', callback_data='product_buying'),
        InlineKeyboardButton(text='Product3', callback_data='product_buying'),
        InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ]
)

#
kbl = InlineKeyboardMarkup(resize_keyboard=True) # создать клавиатуру и авторазмер
but3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
but4 = InlineKeyboardButton(text='формула расчёта', callback_data='formulas')
kbl.row(but3, but4) #

#
@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    textp = 'Название: Product 1 | Описание: описание 1 | Цена: '
    with open('files/watermelon.png', 'rb') as img1 :
        await message.answer_photo(
            img1, f'Название: Product 1 | Описание: описание 1 | Цена: {1 * 100}')
    with open('files/blueberry.png', 'rb') as img2 :
        await message.answer_photo(
            img2, f'Название: Product 2 | Описание: описание 2 | Цена: {2 * 100}')
    with open('files/carrot.png', 'rb') as img3 :
        await message.answer_photo(
            img3, f'Название: Product 3 | Описание: описание 3 | Цена: {3 * 100}')
    with open('files/cherry.png', 'rb') as img4 :
        await message.answer_photo(
            img4, f'Название: Product 4 | Описание: описание 4 | Цена: {4 * 100}',
            reply_markup=catalog_kb)
#
@dp.callback_query_handler(text='product_buying') # обработчик кнопки but4
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()
#
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kbr)
#
@dp.message_handler(text=['Информация'])
async def price(message):
    with open('files/walter-white.png', 'rb') as img :
        await message.answer_photo(img, 'это просто тренировочный БОТ !', reply_markup=kbr)
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
# Пример результата выполнения программы:
#
# Обновлённое главное меню:
#
# привет !
# Введите команду /start, чтобы начать общение.
# /start
#
# привет! я бот помогающий твоему здоровью.
#
# РАССЧИТАТЬ     ИНФОРМАЦИЯ
#     К  У  П  И  Т  Ь
#
# Список товаров и меню покупки:
#
#  Product 1 | Описание: описание 1 | Цена: 1 * 100>
#  ************* К А Р Т И Н К А  1 ****************
#   Выберите продукт для покупки:
#
#  Product 2 | Описание: описание 2 | Цена: 2 * 100>
#  ************* К А Р Т И Н К А  2 ****************
#   Выберите продукт для покупки:
#
#  Product 3 | Описание: описание 3 | Цена: 3 * 100>
#  ************* К А Р Т И Н К А  3 ****************
#   Выберите продукт для покупки:
#
#  Product 4 | Описание: описание 4 | Цена: 4 * 100>
#  ************* К А Р Т И Н К А  4 ****************
#   Выберите продукт для покупки:
#
#
#   "Вы успешно приобрели продукт!"
#
#
# Примечания:
#
#     Название продуктов и картинок к ним можете выбрать самостоятельно.
#     (Минимум 4)
#
# Файл module_14_3.py с кодом загрузите на ваш GitHub репозиторий.
# В решении пришлите ссылку на него.

