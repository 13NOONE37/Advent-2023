file = open('input.txt','r')
lines = file.readlines()

total = 0

for line in lines:
    line = line.split(':')[1]
    line = line.split('|')

    winning_numbers=set()
    for number in line[0].strip().split(' '):
        if number:
            winning_numbers.add(int(number))

    selected_numbers=set()
    for number in line[1].strip().split(' '):
        if number:
            selected_numbers.add(int(number))
    
    length_of_union = len(winning_numbers&selected_numbers)

    if length_of_union==0:
        continue
    points=2**(length_of_union-1)
    total+=points




print(f'The result is {total}')
