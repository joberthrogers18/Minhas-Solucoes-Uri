
def queue(inpt):

    split = inpt.split(" ")

    list_ani = []

    for i in range(str(split[0])):

        list_ani.append({"number": i, "choose": False})



inpt = ''

while(inpt != '0 0 0'):

    inpt = str(input())

