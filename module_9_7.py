
##
# Задание:
# Напишите 2 функции:
#
#     - Функция, которая складывает 3 числа (sum_three)
#     - Функция декоратор (is_prime), которая распечатывает "Простое",
#     если результат 1ой функции будет простым числом и "Составное" в противном случае.
#
###
def is_prime(fun) :
    def wrapper(a, b, c) :
        n = a+b+c
        if n < 2: return f'Несоответствующее \n{n}'
        for i in range(2, n) :
            if n % i == 0 : return f'Составное \n{n}'
        return f'Простое \n{n}'
    return wrapper
#
@is_prime
def sum_three(a, b, c) :
    n = int(a) + int(b) + int(c)
    return n
#
result = sum_three(2, 3, 6)
print(result)
##
#result = is_prime(sum_three(2, 3, 6))
#print(result)
###
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечания:
#
#     Не забудьте написать внутреннюю функцию wrapper в is_prime
#     Функция is_prime должна возвращать wrapper
#     @is_prime - декоратор для функции sum_three
#
#
#     конец задачи
#
