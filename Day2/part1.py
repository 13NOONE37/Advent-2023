lines = open('input.txt','r').readlines()

max_values = {'red':12,'green':13,'blue':14}
total = 0

for line in lines:
    is_possible = True

    line = line.split(':')
    game_id = line[0].split(' ')[1]

    line = line[1].replace(';',',').split(',')
    for value in line:
        amount, name = value.strip().split(' ')
        amount = int(amount)

        if amount >max_values[name]:
            is_possible=False
  
    if is_possible:
        total+=int(game_id)

print(f'The result is: {total}')