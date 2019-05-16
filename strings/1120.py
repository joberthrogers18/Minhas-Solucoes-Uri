if __name__ == '__main__':

    process_number = []

    current_input =''

    while(1):
        contability =  str(input())

        if(contability == '0 0'):
            break

        split_number = contability.split(" ")

        split_number[1] = split_number[1].replace(split_number[0],'')

        if(split_number[1] == ''):
            process_number.append('0')   
            continue      

        process_number.append(split_number[1])
    
    for cont in process_number:
        print(int(cont))
