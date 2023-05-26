with open('book.txt', 'r', encoding='utf-8') as file:
    data = file.read()
print(data)
data = data.split('\n')[1::]
print(data)