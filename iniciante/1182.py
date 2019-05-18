
colum  = int(input())

operation = str(input())

matrix = []

for i in range(12):

    aux = []

    for j in range(12):

        aux.append(float(input()))

    matrix.append(aux)

value = 0

for item in matrix:

    value += item[colum]

if operation == 'S':
    print("%.1f"%(value))
elif operation == 'M':
    print("%.1f"%(value/12))