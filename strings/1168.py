dict_guide = {"0": 6, "1": 2, "2": 5, "3":5 , "4": 4, "5": 5, "6":6, "7":3, "8":7, "9":6}

number_inputs = int(input())

i = 0

while(i < number_inputs):

    current_leds = str(input())
    number_leds = 0

    for number in current_leds:
        number_leds += dict_guide[number]

    print("%d leds"%(number_leds))

    i += 1
