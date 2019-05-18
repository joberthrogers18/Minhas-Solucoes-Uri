
def transformBinary(number):

    stack = []
    stack.append(number % 2)
    number_c = number // 2

    for i in range(31):
        stack.append(number_c % 2)
        number_c = number_c // 2

    return stack

def calculate(get_numbers):
    split_numbers = get_numbers.split(" ")

    number1 = split_numbers[0]
    number2 = split_numbers[1]

    bin1 = transformBinary(int(number1))
    bin2 = transformBinary(int(number2))

    result = []

    for i in range(len(bin1)):

        if bin1[i] == bin2[i]:
            result.append(0)
            continue
        
        result.append(bin1[i] + bin2[i])

    sum_final = 0

    for i in range(len(result)):
        if result[i]:
            sum_final += 2**i

    return sum_final



while(1):

    try:
        get_numbers = str(input())
        print(calculate(get_numbers))
    except EOFError:
        exit()




