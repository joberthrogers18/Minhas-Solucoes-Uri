number = int(input())

operator = str(input())

matrix = []

for i in range(12):

    aux = []

    for j in range(12):

        aux.append(float(input()))

    matrix.append(aux)

if operator == 'S':
    print("%.1f"%(sum(matrix[number])))
elif operator == 'M':
    print("%.1f"%( sum(matrix[number]) / 12))

        