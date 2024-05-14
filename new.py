# TODO условные операторы
# if (логическая переменная):
# переменная, если логическая операция == True

# if (логическая переменная):
# переменная, если логическая операция == True
# else:
#  операция, если переменная == False


value_bool_1 = True
if value_bool_1:
    print("правда 1")

value_bool_1 = False
if value_bool_1:
    print("правда 2")
else:
    print("Ложь2")

# TODO циклы

# перечисляемый цикл, или цикл for
# for (переменная, которая будет содержать каждый раз, разное значение из итератора) in (итератор - объект по которому проходятся циклом)
# логика которая выполняется каждую итерацию - повторение цикла

for i in [2, 3, 4, 5, 6]:
    print(i)

str_value_1 = "Many яблок"

for char_element in str_value_1:
    print(char_element)

str_value_2 = [[2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6]]
for first_loop in str_value_2:
    # print(first_loop)
    for second_loop in first_loop:
        print(second_loop)

str_value_2 = [["1_1", "1_2", "1_3", "1_4", "1_5"], ["2_1", "2_2", "2_3", "2_4", "2_5"]]
for first_loop in str_value_2:
    # вторая итерация (повторение цикла) не запустится, пока вложенный цикл не отработает полностью
    for second_loop in first_loop:
        print(second_loop)

# TODO условный цикл WHILE
# условный цикл while("пока")

while_continue = True
index = 0
while while_continue:
    index = index + 2
    print(index)
    # index += 2
    if index >= 30:
        while_continue = False
