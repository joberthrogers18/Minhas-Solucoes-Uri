operator = str(input())

matrix = []

for i in range(12):

    aux = []

    for j in range(12):

        aux.append(float(input()))

    matrix.append(aux)

sum_all = 0
cont = 0
size = 0

for i in range(5):
    aux = []
    for j in range(1 + size, 11 - size):
        sum_all += matrix[j][i]
        cont += 1
    size += 1


if operator == 'S':
    print("%.1f"%(sum_all))
elif operator == 'M':
    print("%.1f"%( sum_all / cont))

        