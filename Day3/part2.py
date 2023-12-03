file = open('input.txt','r').read()
lines = file.split('\n')

def find_number(current_x,current_y):
    digits = [lines[current_y][current_x]]
    length_of_line = len(lines[current_y])

    for x in range(current_x-1, -1, -1):
        char = lines[current_y][x]
        if not char.isnumeric():
            break 
        digits.insert(0,char)

    for x in range(current_x+1, length_of_line):
        char = lines[current_y][x]
        if not char.isnumeric():
            break
        digits.append(char)

    return max(1, int(''.join(digits)))

def get_gear_ratio(current_x,current_y):
    y_start = max(0,current_y-1)
    y_end = min(len(lines),current_y+2)
    part_numbers = set()

    for y in range(y_start,y_end):
      x_start = max(0,current_x-1)
      x_end = min(len(lines[y]),current_x+2)

      for x in range(x_start,x_end):
         char = lines[y][x]
         if char.isnumeric():
            part_numbers.add(find_number(x,y))
    
    if len(part_numbers)>=2:
        result = 1 

        for number in part_numbers:
            result*=number
        return result
    
    return 0

total = 0

for y in range(0,len(lines)):
    for x in range(0,len(lines[y])):
      char = lines[y][x]
      if char=='*':
         total+=get_gear_ratio(x,y)

print(f'The result is {total}')