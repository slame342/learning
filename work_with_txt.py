# with open('C:/project/learn1/learning/file.txt') as file:  # абсолютный путь к файлу с внешней директории
# with open('src/file.txt') as file:  # читает с текущей директории, относительный путь к файлу
# with open('file.txt') as file:  # читает с внешней директории
# text = file.readline()  # читает выбранную строку
# print(text)

# with open('src/dist/file.txt') as file:  # псевдоним
#     text = file.readline()  # читает все строки, возвращает массив
#     print(text)


with open('file.txt') as file:  # псевдоним
    text = file.readlines()  # читает все строки, выдает массив
    print(text)

    new_list = []
    for line in text:
        if len(line) > 1:
            new_list.append(line[0:-1:1])  # добавление нового объекта в список в конец
            # print(line[0:-1:1])
    print(new_list)

    # text1 = text[начало:конец:шаг]

    # text = "Pellentesque"
    # text1 = text[3::1]  # обрезает строку в обычной последовательности от 3 символа до
    # print(text1)

    # text = "Pellentesque"
    # text1 = text[3:10:1]  # обрезает строку в обычной последовательности от 3 до 10 символа
    # print(text1)

    # text = "Pellentesque"
    # text1 = text[:0:-1]  # обрезает строку в обратной последовательности
    # print(text1)

    # text = "Pellentesque"
    # text1 = text[1:-3:1]
    # print(text1)

    print('\nHello\fWorld\t')  # спец символы в строках

# with open('src/dist/new_file.txt', 'a') as file:
#     list_1 = ['Астана', 'Караганда', 'Чимкент', 'Актюбинск', 'Астана', 'Караганда', 'Чимкент', 'Актюбинск']
#     file.write('\nlist_12698463')

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)
# print(newlist)

# list comprehension
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
# newlist = [x for x in fruits]
# newlist = [(x + '1') for x in fruits if'a' in x]
newlist = [(fruit + '$ 1') for fruit in fruits if 'a' in fruit]
print(newlist)

# list comprehension
with open('src/dist/new_file1.txt', 'a', encoding='utf-8') as file:
    list_1 = ['Астана', 'Караганда', 'Чимкент', 'Актюбинск', 'Астана', 'Караганда', 'Чимкент', 'Актюбинск']
    file.writelines([f'{city}\n' for city in list_1])

# обработка через цикл
# with open('src/dist/new_file1.txt', 'a', encoding='utf-8') as file:
#     list_1 = ['Астана', 'Караганда', 'Чимкент', 'Актюбинск', 'Астана', 'Караганда', 'Чимкент', 'Актюбинск']
#     newlist = []
#     for city in list_1:
#         newlist.append(f'{city}\n')
#     file.writelines(newlist)

# text = file.write()
# text = file.read()

index = 0
text = 'EkibastuzEkibastuzEkibastuz'
new_text = " "
# for char in text:
#     index = index + 1
#     new = index%2
#     new_char = ' '
#     if new == 0:
#         new_char =
#         new_text += new_char
# print(new_text)


new_list1 = [f"1{char}" for char in text if text.index(char) % 2 != 0]

print(' '.join(new_list1))

# практическое задание 4.1
# list_1 = ['Астана', 'Караганда', 'Чимкент', 'Актюбинск']
# print(list_1[::-1])

# практическое задание 4.2
# list_1 = ['Астана', 'Караганда', 'Чимкент', 'Актюбинск']
# print(len(list_1))
