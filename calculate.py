def calc(number1, number2, operations):
    if operations == "+":
        return number1 + number2
    if operations == "-":
        return number1 - number2
    if operations == "*":
        return number1 * number2
    if operations == "**":
        return number1 ** number2
    if operations == "/":
        if number2 != 0:
            return number1 / number2
        else:
            print('Error!')
            return 0
    if operations == "//":
        if number2 != 0:
            return number1 // number2
        else:
            print('Error!')
            return 0


result = calc(5, 10, "+")
print(result)
result = calc(9, 6, "-")
print(result)
result = calc(2, 2, "*")
print(result)
result = calc(3, 2, "**")
print(result)
result = calc(33, 0, "/")
print(result)
result = calc(33, 2, "//")
print(result)

