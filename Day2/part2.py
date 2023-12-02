lines = open('input.txt','r').readlines()

total = 0

for line in lines:
    line = line.split(':')
    game_id = line[0].split(' ')[1]

    line = line[1].replace(';',',').split(',')
    
    max_red=0
    max_green=0
    max_blue=0

    for value in line:
        amount, name = value.strip().split(' ')
        amount = int(amount)

        if name=='red' and amount>max_red:
            max_red = amount
        if name=='green' and amount>max_green:
            max_green = amount
        if name=='blue' and amount>max_blue:
            max_blue = amount
            
    total+=(max_red*max_green*max_blue)

print(f'The result is: {total}')