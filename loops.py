# 0   1  2    3
from logic_operations import var_1

var_list1 = [12, 0, 16, 8, '1234', -100, True]  # массив переменных

# for list_element in var_list1:
#     print('element:', var_list1.index(list_element), type(list_element), list_element)


# цикл, который итерируется по массиву объектов
# и берет каждый цикл себе в переменную (list_element)
for list_element in (12, 16, 8, -100):
    for list_element1 in var_list1:
        print('element:', var_list1.index(list_element), type(list_element), list_element)
    # kod do cikla
    for list_element1 in var_list1:
        # kod v cikle
        print('element:', var_list1.index(list_element1), type(list_element1), list_element1)
    # kod posle cikla

# var_int1 = 12
#     while var_int1:
#     var_int1 = var_int1 - 1
#     print(var_int1)
# print('цикл завершен!')

# var_int1 = 12
# while var_int1 < 56:
#     var_int1 = var_int1 + 1
#     print(var_int1)
#     if var_int1 == 56:
#         print('end')
#
# print('цикл завершен!')


# list_1 = ['Астана', 'Караганда', 'Чимкент', 'Актюбинск']
#
# index_i = 0
# for i in list_1:
#     print(i + " " + str(list_1.index(i) + 1))
# # index_i += 1
# string_city = f"{i} {list_1.index(i) + 1}"
# print(string_city)
# print(i + " " + str(list_1.index(i) + 1))


# # практическое задание с циклами 1
# list_2 = [input('введите число 1: '), input('введите число 2: ')]
#
# for i in list_2:
#     print(i)
#
# # практическое задание с циклами 2
# list_3 = [input('введите число 1: '), input('введите число 2: ')]
# # list_3 = [15, 14]
# for i in list_3:
#     if int(i) % 2 >= 0:
#         print(str(i) + ' ' + 'нечетное число')
#
# # практическое задание с циклами 3
# list_4 = [input('введите число 1: '), input('введите число 2: ')]
# # list_4 = [15, 14]
# for i in list_4:
#     if int(i) % 2 == 0:
#         print(str(i) + ' ' + 'четное число')

# практическое задание с циклами 4
# list_5 = [input('введите число 1: '), input('введите число 2: ')]
# list_5 = [12, 43]
