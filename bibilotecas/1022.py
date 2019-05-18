
def calculate(expression):

    split_exp = expression.split(" ")

    numerators = []
    character = []

    for i in range(len(split_exp)):
        if i % 2 == 0:
            numerators.append(split_exp[i])
        else:
            character.append(split_exp[i])

    numerator = 0
    denominator = 0

    if character[1] == '+':
        numerator = (
            int(numerators[0]) * int(numerators[3]) + int(numerators[1])*int(numerators[2]))
        denominator = (int(numerators[1])*int(numerators[3]))
        mdc = MDC(numerator, denominator)

        if denominator < 0:
            denominator *= -1
            numerator *= -1

        return f"{numerator}/{denominator} = {int(numerator / mdc)}/{int(denominator / mdc)}"
    elif character[1] == '-':
        numerator = (
            int(numerators[0]) * int(numerators[3]) - int(numerators[1])*int(numerators[2]))
        denominator = (int(numerators[1])*int(numerators[3]))
        mdc = MDC(numerator, denominator)

        if denominator < 0:
            denominator *= -1
            numerator *= -1

        return f"{numerator}/{denominator} = {int(numerator / mdc)}/{int(denominator / mdc)}"
    elif character[1] == '*':
        numerator = (int(numerators[0]) * int(numerators[2]))
        denominator = (int(numerators[1])*int(numerators[3]))
        mdc = MDC(numerator, denominator)

        if denominator < 0:
            denominator *= -1
            numerator *= -1

        return f"{numerator}/{denominator} = {int(numerator / mdc)}/{int(denominator / mdc)}"
    elif character[1] == '/':
        numerator = (int(numerators[0]) * int(numerators[3]))
        denominator = (int(numerators[2])*int(numerators[1]))
        mdc = MDC(numerator, denominator)

        if denominator < 0:
            denominator *= -1
            numerator *= -1

        return f"{numerator}/{denominator} = {int(numerator / mdc)}/{int(denominator / mdc)}"


def MDC(number1, number2):

    a = max(number1, number2)
    b = min(number1, number2)

    try:
        if(a % b == 0):
            return abs(b)
        else:
            return MDC(b, (a % b))
    except ZeroDivisionError:
        return 1


number_itteration = int(input())
i = 0

list_all = []

while(i < number_itteration):
    input_exp = str(input())
    list_all.append(calculate(input_exp))
    i += 1

for let in list_all:
    print(let)
