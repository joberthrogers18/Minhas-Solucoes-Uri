operator = str(input())

matrix = []

for i in range(12):

    aux = []

    for j in range(12):

        aux.append(float(input()))

    matrix.append(aux)

i = 0
sum_all = 0
cont = 0

for i in range(6):
    for j in range(1 + i, 11 - i):
        sum_all += matrix[i][j]
        cont += 1
    i+= 1

if operator == 'S':
    print("%.1f"%(sum_all))
elif operator == 'M':
    print("%.1f"%( sum_all / cont))

        