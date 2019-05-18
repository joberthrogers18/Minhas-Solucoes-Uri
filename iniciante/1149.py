

entry = str(input()).split(" ")

while(int(entry[-1]) <= 0):
    entry[-1] = str(input())

total_sum = 0

for i in range(0, int(entry[-1])):
    total_sum += i + int(entry[0])

print(total_sum)