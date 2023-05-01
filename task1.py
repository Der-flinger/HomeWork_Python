# Задача 26:  Напишите программу, которая на вход принимает два 
# числа A и B, и возводит число А в целую степень B с помощью рекурсии.


def exponent(num, degree):
    if degree == 1:                                 # работает и для отлрицательных чисел
        return num
    if degree < 0:
        return 1 / exponent(num, -degree)
    if degree != 1:
        return num * exponent(num, degree - 1)
print(exponent(5, -1))