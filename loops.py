# 0   1  2    3
var_list1 = [12, 0, 16, 8, '1234', -100, True]  # массив переменных

# for list_element in var_list1:
#     print('element:', var_list1.index(list_element), type(list_element), list_element)


# цикл который итерируется по массиву обьектов
# и берет каждый цикл себе в переменную (list_element)
# for list_element in (12, 16, 8, -100)
for list_element in var_list1:
    print('element:', var_list1.index(list_element), type(list_element), list_element)
    # kod do cikla
    for list_element1 in var_list1:
        # kod v cikle
        print('element:', var_list1.index(list_element1), type(list_element1), list_element1)
#       kod posle cikla


# var_int1 = 12
#     while var_int1:
#     var_int1 = var_int1 - 1
#     print(var_int1)
# print('цикл завершен!')

var_int1 = 12
while var_int1 < 56:
    var_int1 = var_int1 + 1
    print(var_int1)
    if var_int1 == 56:
        print('end')

print('цикл завершен!')
