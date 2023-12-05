file = open('input.txt','r')
lines = file.readlines()

def get_scratchcard_info(line):
    line = line.split(':')
    line_index = int(line[0].split(' ')[-1])-1
    line = line[1].split('|')

    winning_numbers = set()
    selected_numbers = set()
    
    for number in line[0].strip().split(' '):
        if number:
            winning_numbers.add(int(number))
    for number in line[1].strip().split(' '):
        if number:
            selected_numbers.add(int(number))
    matches = len(winning_numbers&selected_numbers)
   
    return line_index, matches

total = 0
# strachcards_status= []
def get_cards(line_index,matches):
    global total
    total+=1

    if matches>0 and line_index<len(lines):
        for i in range(line_index+1,line_index+1+matches):
            _, new_matches = get_scratchcard_info(lines[i])
            get_cards(i,new_matches)

# for line in lines:
#     line_index, matches = get_scratchcard_info(line)
#     strachcards_status.append((line_index,matches>0))


for line in lines:
    line_index, matches = get_scratchcard_info(line)
    get_cards(line_index,matches)

print(f'The result is {total}')
