operator = str(input())

matrix = []

for i in range(12):

    aux = []

    for j in range(12):

        aux.append(float(input()))

    matrix.append(aux)

sum_all = 0
count = 0

for i in range(11, -1, -1):
    
    sum_all += sum(matrix[i][12 - i: : 1])
    count += i


if operator == 'S':
    print("%.1f"%(sum_all))
elif operator == 'M':
    print("%.1f"%(sum_all / count))

        