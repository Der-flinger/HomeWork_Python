# Функции для использования

def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print()
        print(file.read())
        print()

def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input("Введите ФИО - ")
    phone = input("Введите номер телефона - ")
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')

def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print()
    print('\n'.join(data), '\n')
    find_info = input("Введите данные для поиска: ")
    print(search(data, find_info))


def search(book: list[str], info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
    res = [contact for contact in book if info in contact]
    if len(res) > 1:
        print('\n-------------')
        print('\n'.join(res))
        print()
        clarification = input("Введите данные для уточнения: ")
        return search(res, clarification)
    elif len(res) == 1:
        print()
        return res[0]
    else:
        return "Совпадений не найдено"

def change_data() -> None:
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print()
    print('\n'.join(data))
    print()
    data_to_edit = input("Введите данные для поиска ---> ")
    data_to_edit = search(data, data_to_edit)
    print(data_to_edit)
    print()
    mode = input("Введите действие: 1 - удалить, 2 - заменить ---> ")
    if mode == '1':
        data.remove(data_to_edit)
        print('\n'.join(data))
    elif mode == '2':
        data[data.index(data_to_edit)] = enter_change()
        print('\n'.join(data))
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))

def enter_change() -> str:
    fio = input("Введите ФИО: ")
    number = input("Введите номер телефона: ")
    return (f"{fio} | {number}")