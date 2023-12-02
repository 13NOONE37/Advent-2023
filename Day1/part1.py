lines = open('input.txt','r').readlines()

total = 0

for line in lines:
    digit =''

    for char in line:
        if char.isnumeric():
            digit+=char
            break

    for char in line[::-1]:
        if char.isnumeric():
            digit+=char
            break
    total+=int(digit)

print(f'The result is: {total}')
    




