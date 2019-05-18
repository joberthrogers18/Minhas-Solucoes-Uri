string_input = str(input())

split_string = string_input.split("\n")

isUpper= True

for split in split_string:
    if split == '':
        continue

    word_convert = ''

    for char in split:

        if char == ' ':
            word_convert += ' '
            continue
        
        if isUpper:
            word_convert += char.upper()
            isUpper = False
        else:
            word_convert += char.lower()
            isUpper = True

    print(word_convert)
    
    isUpper = True





