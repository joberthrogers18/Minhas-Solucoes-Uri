import time

number_clients = int(input())

chairs = []

response = []
number_chair = 0
i = 0

def sortSecond(val): 
    return val[1] 

def split_hours(teste):   

    split = teste.split(" ")

    aux = (time.strptime(split[0].replace(':', '::'), '%H::%M::%S'), time.strptime(split[1].replace(':', '::'), '%H::%M::%S'))

    if aux[0] > aux[1]:
        aux2 = (aux[1], aux[0])
        response.append(aux2)
        return 

    response.append(aux)

while(i < number_clients ):
    current = str(input())
    split_hours(current)  

    i+= 1

response.sort(key = sortSecond) 

chairs.append(response[0][1])
response.pop(0)

aux = False
while(len(response) != 0):
    cont  = 0
    for i in chairs:
        if i <= response[0][0]:
            chairs[cont] = response[0][1]
            aux = True
        cont += 1
    if aux == False:
        chairs.append(response[0][1])
    else:
        aux = False
    response.pop(0)

print(len(chairs))
            








