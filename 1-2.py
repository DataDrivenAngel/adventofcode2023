# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

######
#
# Solution here it seems to me, is check 'digit' type seperately and record positon, then assemble the results and get first first and last last and create the digits.
#
######

text = open("1-1.txt",'r')
data = text.read().split('\n')
digit_dict = {
    'one':1,
    'two':2,
    'three':3,
    'four':4, 
    'five':5,
    'six':6, 
    'seven':7, 
    'eight':8,
    'nine':9
    }




def number_finder(input_string):
    location_dict = dict()
    for enum, i in enumerate(input_string):
        if str.isnumeric(i) == True:
            x = i
            location_dict.update({enum:x})
    return(location_dict)

def digit_finder(input_string, digit_dict):
    location_dict = dict()
    for digit in list(digit_dict.keys()):
        if digit in input_string:
            pos = input_string.find(digit)
            number = digit_dict[digit]
            location_dict.update({pos:number})
    return(location_dict) 


def get_calibration_sum(input_string, digit_dict):
    location_dict = digit_finder(input_string,digit_dict)

    location_dict.update(number_finder(input_string))

    
    first_int = location_dict[min(location_dict.keys())]
    last_int = location_dict[max(location_dict.keys())]
    calibration_sum = str(first_int) + str(last_int)
    return(calibration_sum)



total_sum = 0
for input_string in data:
    total_sum = total_sum + int(get_calibration_sum(input_string,digit_dict))

print(total_sum)

# 56136 is incorrect
# 55060 is incorrect
# 'eighteight9dnvcqznjvfpreight' is so rude
