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
# Задача "Цепочка вопросов":
# Необходимо сделать цепочку обработки состояний для нахождения нормы калорий
# для человека.
#
# Группа состояний:
#
#     Импортируйте классы State и StatesGroup из aiogram.dispatcher.filters.state.
#     Создайте класс UserState наследованный от StatesGroup.
#     Внутри этого класса опишите 3 объекта класса State:
#     age, growth, weight (возраст, рост, вес).
#
# Эта группа(класс) будет использоваться в цепочке вызовов message_handler'ов.
# Напишите следующие функции для обработки состояний:
# Функцию set_age(message):
#
#     Оберните её в message_handler, который реагирует на текстовое сообщение
#     'Calories'.
#     Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
#     После ожидать ввода возраста в атрибут UserState.age при помощи метода set.
#
# Функцию set_growth(message, state):
#
#     Оберните её в message_handler, который реагирует на переданное состояние
#     UserState.age.
#     Эта функция должна обновлять данные в состоянии age на
#     message.text (написанное пользователем сообщение).
#     Используйте метод update_data.
#     Далее должна выводить в Telegram-бот сообщение 'Введите свой рост:'.
#     После ожидать ввода роста в атрибут UserState.growth при помощи метода set.
#
# Функцию set_weight(message, state):
#
#     Оберните её в message_handler, который реагирует на переданное состояние
#     UserState.growth.
#     Эта функция должна обновлять данные в состоянии growth на message.text
#     (написанное пользователем сообщение). Используйте метод update_data.
#     Далее должна выводить в Telegram-бот сообщение 'Введите свой вес:'.
#     После ожидать ввода роста в атрибут UserState.weight при помощи метода set.
#
# Функцию send_calories(message, state):
#
#     Оберните её в message_handler, который реагирует на переданное состояние
#     UserState.weight.
#     Эта функция должна обновлять данные в состоянии weight на message.text
#     (написанное пользователем сообщение). Используйте метод update_data.
#     Далее в функции запомните в переменную data все ранее введённые состояния
#     при помощи state.get_data().
#     Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий
#     (для женщин или мужчин - на ваше усмотрение).

#      [ Упрощенный вариант формулы Миффлина-Сан Жеора:
#
#     для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
#     для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161. ]
#
#     Данные для формулы берите из ранее объявленной переменной data по ключам
#     age, growth и weight соответственно.
#     Результат вычисления по формуле отправьте ответом пользователю в Telegram-бот.
#     Финишируйте машину состояний методом finish().
#
# !В течение написания этих функций помните, что они асинхронны и все функции
#   и методы должны запускаться с оператором await.
#
# #
# Пример результата выполнения программы:
#
# /start
# привет! я бот помогающий твоему здоровью.
# Calories
# Введите свой возраст:
# 24
# Введите свой рост:
# 178
# Введите свой вес:
# 110
# Ваша норма калорий 2168.48
#
#
#Updates were skipped successfully.
#Goodbye!
#
# Примечания:
#
#     Для ответа на сообщение запускайте метод answer асинхронно.
#     При отправке вашего кода на GitHub не забудьте убрать ключ для
#     подключения к вашему боту!
#
###
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
#
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
#
api = '44444444444444444444444444444444444444444444444444'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
#
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
#
@dp.message_handler(text=['Calories'])
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
    
    await state.finish()
#
@dp.message_handler()
async def start(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
##
if __name__ == '__main__' :
    executor.start_polling(dp, skip_updates = True) # для v 2.25
#
###
