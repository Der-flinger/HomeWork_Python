# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
N = int(input("Введите кол-во эл-ов массива - "))
minNum = int(input("Введите мин. значение - "))
maxNum = int(input("Введите макс. значение - "))
nums = list(random.randint(minNum, maxNum) for i in range(N))
print(nums)
x = int(input("Введите число X - "))
diff = nums[0]
for i in nums:
    if abs(i - x) < abs(diff - x):
        diff = i
print(f"Самое близкое к 'X' это - '{diff}'")
