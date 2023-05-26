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