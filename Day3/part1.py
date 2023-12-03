file = open('input.txt','r').read()
lines = file.split('\n')

def check_neighbours(current_y,digit_start,digit_end):
    y_start = max(0,current_y-1)
    y_end = min(len(lines),current_y+2)

    for y in range(y_start,y_end):
      x_start = max(0,digit_start-1)
      x_end = min(len(lines[y]),digit_end+1)

      for x in range(x_start,x_end):
         char = lines[y][x]
         if not char.isnumeric() and char!='.':
           return True
    return False

total = 0

for y in range(0,len(lines)):
    digit = ''
    digit_start = digit_end = -1

    for x in range(0,len(lines[y])):
      char = lines[y][x]

      if char.isnumeric():
        if not digit:
           digit_start=x
        digit+=char

      if not char.isnumeric() or x == len(lines[y])-1:
        digit_end=x
        if digit and -1 < digit_start < len(lines[y]) and -1 < digit_end < len(lines[y]):
            if check_neighbours(y, digit_start, digit_end):
               total += int(digit)

        digit=''
        digit_start = digit_end = -1

print(f'The result is {total}')