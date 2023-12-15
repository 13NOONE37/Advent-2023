file = open('input.txt','r')
lines = [line for line in file.read().split('\n')]

def is_arrangement_correct(row,lengths):
    row_lengths = []
    for string in row.split('.'):
        if string:
            row_lengths.append(len(string))
    return row_lengths==lengths

def generate_options(row):
    result = []

    def generate_helper(current,index):
        if index == len(row):
            #When we reach the end
            result.append(''.join(current))
            return
        
        if row[index] == '?':
            #When we meet '?'
            current[index] = '.'
            generate_helper(current,index+1)
            current[index]='#'
            generate_helper(current, index+1)
        else:
            #If char is diffrent we call function with next function
            generate_helper(current, index+1)

    generate_helper(list(row),0)
    return result

possible_arrangments = 0
for line in lines:
    row, lengths = line.split(' ')
    lengths = [int(n) for n in lengths.split(',')]
    options = generate_options(row)

    for option in options:
        if is_arrangement_correct(option,lengths):
            possible_arrangments+=1

print(f'The sum of total possible arrangments is: {possible_arrangments}')
file.close()