lines = open('input.txt','r').readlines()

total = 0
VALID_DIGITS = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
    }

def find_occurences(string,substring):
    occurrences = []
    index = -1
    while True:
        index = string.find(substring,index+1)

        if index==-1:
            break
        occurrences.append((substring,index))
    
    return occurrences

for line in lines:
    indexes = []

    for element in VALID_DIGITS.keys():
        if element in line:
            indexes+=find_occurences(line,element)

    first_digit = VALID_DIGITS[min(indexes,key=lambda x: x[1])[0]]
    last_digit = VALID_DIGITS[max(indexes,key=lambda x: x[1])[0]]
   
    total+=int(first_digit+last_digit)

print(f'The result is: {total}')
    




