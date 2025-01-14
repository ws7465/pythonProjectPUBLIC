import sqlite3
import random


def initiate_db() :

    connection = sqlite3.connect('module_14_4.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL, 
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    cursor.execute('DELETE FROM Products')

    for i in range(1, 5):
        cursor.execute(
            'INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
            (f'title_{i}', f'description_{i}', f'{i * 100}'))

    connection.commit()
    connection.close()
#
def get_all_products() :

    connection = sqlite3.connect('module_14_4.db')
    cursor = connection.cursor()

    cursor.execute('SELECT id, title, description, price FROM Products')
    ids = cursor.fetchall()
    for id in ids:
        print(f'| Название : {id[1]} | Описание : {id[2]} | Цена : {id[3]} |')

    connection.commit()
    connection.close()

    return ids
#
# connection.commit()
# connection.close()