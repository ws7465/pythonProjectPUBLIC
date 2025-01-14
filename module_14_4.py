####
# Задача "Продуктовая база":
# Подготовка:
# Для решения этой задачи вам понадобится код из предыдущей задачи.
# Дополните его, следуя пунктам задачи ниже.
# Дополните ранее написанный код для Telegram-бота:
# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db, которая создаёт таблицу Products, если она ещё не создана при
#       помощи SQL запроса. Эта таблица должна содержать следующие поля:
# 1.	id - целое число, первичный ключ
# 2.	title(название продукта) - текст (не пустой)
# 3.	description(описание) - текст
# 4.	price(цена) - целое число (не пустой)
# get_all_products, которая возвращает все записи из таблицы Products,
#   полученные при помощи SQL запроса.
#
# Изменения в Telegram-бот:
# 1.	В самом начале запускайте ранее написанную функцию get_all_products.
# 2.	Измените функцию get_buying_list в модуле с Telegram-ботом, используя
#           вместо обычной нумерации продуктов функцию get_all_products.
#           Полученные записи используйте в выводимой надписи:
#           "Название: <title> | Описание: <description> | Цена: <price>"
#
# Перед запуском бота пополните вашу таблицу Products 4 или более записями
#   для последующего вывода в чате Telegram-бота.
#
####
import sqlite3
import crud_functions
#
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
api = '444444444444444444444444444444444444444444'
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
##

crud_functions.initiate_db()
#

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    ids = crud_functions.get_all_products()
    i = 0
    for id in ids:
        i += 1
        file = f'files/{i}.png'
        with open(file, 'rb') as img:
            await message.answer_photo(
                img, f'| Название: {id[1]} | Описание: {id[2]} | Цена: {id[3]} |\n')
    await message.answer('Выберите продукт для покупки:', reply_markup=catalog_kb)

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
# Пример результата выполнения программы:
# Добавленные записи в таблицу Product и их отображение в Telegram-bot:
#
#  ************* К А Р Т И Н К А  1 ****************
#  Product 1 | Описание: описание 1 | Цена: 1 * 100>

#   Выберите продукт для покупки:
#
#  ************* К А Р Т И Н К А  2 ****************
#  Product 2 | Описание: описание 2 | Цена: 2 * 100>

#   Выберите продукт для покупки:
#
#  ************* К А Р Т И Н К А  3 ****************
#  Product 3 | Описание: описание 3 | Цена: 3 * 100>

#   Выберите продукт для покупки:
#
#  ************* К А Р Т И Н К А  4 ****************
#  Product 4 | Описание: описание 4 | Цена: 4 * 100>

#   Выберите продукт для покупки:
#
#
#   "Вы успешно приобрели продукт!"
#
#
# Примечания:
#
#	Название продуктов и картинок к ним можете выбрать самостоятельно.
#       (Минимум 4)
#   Файлы module_14_4.py, crud_functions.py, а также файл с базой данных
#   и таблицей Products загрузите на ваш GitHub репозиторий.
#   В решении пришлите ссылку на него.
#
#
