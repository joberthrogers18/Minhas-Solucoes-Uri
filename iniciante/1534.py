
number_input = int(input())

line = ''
line += '1' + (number_input - 2) * '3' + '2' 

postion1_swap = 0
postion2_swap = len(line) - 1
new = ''

def swap(string, i, j):
    lst = list(string)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)
    
print(line)
while(postion1_swap != len(line) - 1):
    line = swap(line, postion1_swap, postion1_swap + 1)
    postion1_swap += 1
    print(line)