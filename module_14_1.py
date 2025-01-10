###
# Задача "Первые пользователи":
# Создайте файл базы данных not_telegram.db и подключитесь к ней,
#   используя встроенную библиотеку sqlite3.
# Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
# Создайте таблицу Users, если она ещё не создана. В этой таблице должны
#   присутствовать следующие поля:
#
#     id - целое число, первичный ключ
#     username - текст (не пустой)
#     email - текст (не пустой)
#     age - целое число
#     balance - целое число (не пустой)
#
# Заполните её 10 записями:
# User1, example1@gmail.com, 10, 1000
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 1000
# ...
# User10, example10@gmail.com, 100, 1000
#
# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# User1, example1@gmail.com, 10, 500
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 500
# ...
# User10, example10@gmail.com, 100, 1000

# Удалите каждую 3ую запись в таблице начиная с 1ой:
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 500
# User5, example5@gmail.com, 50, 500
# ...
# User9, example9@gmail.com, 90, 500
#
# Сделайте выборку всех записей при помощи fetchall(),
#   где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
#
###

import sqlite3
import random

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY, 
username TEXT NOT NULL, 
email TEXT NOT NULL,
age INTEGER,
balance TEXT NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

cursor.execute('DELETE FROM Users')

for i in range(1, 11) :
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i*10}', f'{i*100}'))

cursor.execute('UPDATE Users SET balance = ? WHERE (id % 2) <> 0', (500,))

cursor.execute('DELETE FROM Users WHERE id = 1 OR (id % 3) = 1')

#UPDATE goods SET price = price / 2 WHERE price >= 100

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <> ?', (60,))
users = cursor.fetchall()
for user in users :
    print(f'Имя:  {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()

###
# Пример результата выполнения программы:
# Вывод на консоль:
# Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
# Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
# Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
# Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
# Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500
###
