var_bool1 = True
var_bool2 = False

# integer
var_int1 = 12
var_int2 = -10

# float
var_float1 = 12.14
var_float2 = -10.00
var_float3 = 0.0

# string
var_str1 = " "
var_str2 = "Иван"
var_str3 = "12"
var_str4 = "Anatoliy"
var_str5 = "The're"
var_str6 = 'The"re'
var_str7 = """The're"""

# list - список
var_list1 = [12, 16, 0, -100]
var_list2 = [12, True, 0, -10.00]

# list - кортеж (реизменяемый тип данных)
var_tuple1 = [12, 16, 0, -100]
var_tuple2 = [12, True, 0, -10.00]

# dict - словарь
var_dict1 = {
    "first key": "Иван",
    "second key": "Иван",
    "three key": "[12, True, 0, -10.00]",
    "four key": {
        "first key": "Иван",
        "second key": "Иван",
        "three key": "[12, True, 0, -10.00]",
        "four key": "Иван"
    },
    "five key": "Иван",
}

# constant - условно неизменяемая переменная
VAR_TUPLE1 = [12, 16, 0, -100]
# var_tuple2 = [12, True, 0, -10.00]

var_bool1 = True
var = type(var_bool1)
print(var)

# print(type([12]))