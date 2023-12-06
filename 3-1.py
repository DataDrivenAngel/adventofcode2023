# --- Day 3: Gear Ratios ---

# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?


text = open("3-1.txt",'r')
data = text.read().split('\n')


schematic = [list(row) for row in data]
symbol_list = ''
valid_parts = []
for enumer,row in enumerate(data):
    #print(enumer)
    row = row.replace('.','')
    for char in row:
        if char.isdigit() == False and char not in symbol_list:
            symbol_list = symbol_list + char
            


def adjacency_list_builder(data,row,character):
    cenum = character
    char = character
    renum = row
    top = ''
    mid = ''
    bot = ''
    adjacents = ''
    #top
    if renum != 0:
        if char == 0:
            top = data[renum-1][cenum:cenum+2]
        elif char == 139:
            top = data[renum-1][cenum-1:cenum+1]
        else:
            top = data[renum-1][cenum-1:cenum+2]
    

    # middle row
    if char == 0:
        mid =  data[renum][cenum+2]
    elif char == 139:
        mid =  data[renum][cenum]
    else:
        mid = data[renum][cenum-1:cenum+2]


    #bottom row
    if renum != 139:
        if char == 0:
            bot =  data[renum+1][cenum:cenum+2]
        elif char == 139:
            bot =  data[renum+1][cenum-1:cenum+1]
        else:
            bot =  data[renum+1][cenum-1:cenum+2]



    adjacents = top + mid + bot


    return(adjacents)


for renum, row in enumerate(schematic):
    current_part_max = 0
    for cenum, char in enumerate(row):

        part = ''
        if char.isdigit() == True and current_part_max < cenum :
            current_part_max = cenum + 1
            
            part = char 
            part_length = 0
            
            if  cenum < 137 and row[cenum+1].isdigit():
                part = part + row[cenum+1]
                part_length = 1

            if  cenum < 138 and row[cenum+2].isdigit():
                part = part + row[cenum+2]
                part_length = 2
            
            
            for space in range (0, part_length):
                adjacents = adjacency_list_builder(data = data, row = renum, character = cenum )
                #check adjacent character for news
                for adj_chart in adjacents:
                    if adj_chart in symbol_list:
                        valid_parts.append(int(part))
                        
                        break
                break

total = 0
for part in valid_parts:
    total = total + part
print(total)