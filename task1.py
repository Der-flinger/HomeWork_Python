# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем на следующией строке второй список.

import random

method = int(input(f"Введите 1 или 2 для ввода элементов с клавиатуры или слуйчайно: "))
match (method):
    case 1:
        list1 = [int(i) for i in input().split()]
        print(f"Первый массив: {list1}")
        list2 = [int(i) for i in input().split()]
        print(f"Второй массив: {list2}")
    case 2:
        list1 = [random.randint(1, 10) for i in range(20)]
        print(f"Первый массив: {list1}")
        list2 = [random.randint(1, 10) for i in range(20)]
        print(f"Второй массив: {list2}")
    case _:
        raise TypeError("Неверная команда, введите еще раз")


res = set(list1).intersection(set(list2)) 
print(f"Результирующий массив: {res}")