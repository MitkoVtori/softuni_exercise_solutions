from math import floor


def multiply():
    global sentence

    manual_check = " * ".join([str(num) for num in sentence])
    result = 1

    for item in sentence:
        result *= int(item)

    manual_check += f" = {result}"
    return manual_check, result


def add():
    global sentence

    manual_check = " + ".join([str(num) for num in sentence])
    result = sum([int(num) for num in sentence])

    manual_check += f" = {result}"
    return manual_check, result


def divide():
    global sentence

    manual_check = " / ".join([str(num) for num in sentence])
    result = int(sentence[0])

    try:

        for index in range(len(sentence)):
            result /= int(sentence[index+1])

    except IndexError:
        manual_check += f" = {result}"
        return manual_check, result


def subtract():
    global sentence

    manual_check = " - ".join([str(num) for num in sentence])
    result = int(sentence[0])

    try:

        for index in range(len(sentence)):
            result -= int(sentence[index+1])

    except IndexError:
        manual_check += f" = {result}"
        return manual_check, result


sentence = []

operations = {
    "*": multiply,
    "+": add,
    "/": divide,
    "-": subtract
}

expression = input().split()
result = 0

for item in expression.copy():

    index = expression.index(item)

    if item in operations.keys():
        sentence = expression[0:index]
        result = operations[item]()
        # print(result[0])
        expression = expression[index+1:]
        expression.insert(0, result[1])

print(floor(result[1]))