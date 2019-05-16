
def encode(var):
    transform = ''

    for char in var:
        if char.islower() or char.isupper():
            transform += chr(ord(char) + 3)
        else:
            transform += char

    transform = transform[-1::-1]

    half_list = len(transform) // 2

    new_string = transform[: half_list]

    for i in range(half_list, len(transform)):

        aux = chr(ord(transform[i])-1)
        new_string += aux

    return new_string


if __name__ == '__main__':

    number_search = int(input())
    i = 0

    list_encode = []

    while(i < number_search):
        i+=1
        list_encode.append(encode(str(input())))
        

    for enc in list_encode:
        print(enc)
        
