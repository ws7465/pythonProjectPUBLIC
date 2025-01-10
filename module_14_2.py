# ####
# Задача "Средний баланс пользователя":

# Для решения этой задачи вам понадобится решение предыдущей.
# Для решения необходимо дополнить существующий код:
#
# 1.	Удалите из базы данных not_telegram.db запись с id = 6.
# 2.	Подсчитать общее количество записей.
# 3.	Посчитать сумму всех балансов.
# 4.	Вывести в консоль средний баланс всех пользователей.
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
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{str(random.randint(20, 60))}', f'{i*100}'))

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT (*) FROM Users')
user_c = cursor.fetchall()[0]
#print(user_c[0])
total_users = user_c[0]

cursor.execute('SELECT SUM(balance) FROM Users')
sum_balance = cursor.fetchone()[0]
#print(sum_balance)
all_balances = sum_balance

print(all_balances / total_users)

connection.commit()
connection.close()

# #Пример результата выполнения программы:
#
# Выполняемый код:
#
# # Код из предыдущего задания
# # Удаление пользователя с id=6
# # Подсчёт кол-ва всех пользователей
# # Подсчёт суммы всех балансов
# print(all_balances / total_users)
# connection.close()
# Вывод на консоль:

# 700.0
#
