# Дополнительное
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и
# столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
# идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
# называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, rows=6, columns=6):
    """
    Вывод на экран таблицы определенных значений, заданных по функции
    """
    array = []
    for i in range(rows):
        arr = []
        for j in range(columns):
            arr.append(j + 1 + i)
        array.append(arr)
    for i in range(rows):
        for j in range(columns):
            array[i][j] = operation(array[0][j], array[i][0])
        #     # print(array[i][j], end=' ',)
        # print()
    return array

def show_table(array: list[list[int]]) -> None:
    """
    Презентабельный вывод таблицы в консоли
    """
    print('\n'.join('\t'.join(map(str, row)) for row in array))


res = print_operation_table(lambda x, y: x * y, 10, 10)
show_table(res)