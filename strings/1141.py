
def greter_than(list_word):

    list_word.sort()
    word_dict = {}

    for i in range(len(list_word)):

        word_dict.update({list_word[i]: 0})
        
        for j in range(i, len(list_word)):

            cmp_word = list_word[j][-1:-(len(list_word[i]) + 1) : -1]

            cmp_word = cmp_word[-1::-1]

            # print(list_word[i])
            # print(cmp_word)
            # print('\n\n')
            if(list_word[i] == cmp_word):
                print(list_word[j].count(list_word[i]))
                word_dict[list_word[i]] += 1

    greater = verify_the_greater(word_dict)

    return greater

def verify_the_greater(word_d):

    sorted_dict = sorted(word_d.items(),key= lambda x: x[1])

    return sorted_dict[-1][1]


if __name__ == '__main__':

    list_string_numbers = []

    while(1):

        input_numbers = int(input())

        if input_numbers == 0:
            break

        i = 0

        list_words = []

        while(i < input_numbers):
            word = str(input())
            list_words.append(word)
            i += 1


        list_string_numbers.append(greter_than(list_words))

    for number in list_string_numbers:
        print(number)
    
