# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
array = []
for i in range(1,30):
    array.append(random.randrange(1,10))
print(array)
min_number = int(input("Введите минимальное число - "))
max_number = int(input("Введите максимальное число - "))
res = []
for i in range(len(array)):
    if min_number <= array[i] <= max_number:
        res.append(i)
print("Индексы элементов из диапазона в списке ниже")
print(res)