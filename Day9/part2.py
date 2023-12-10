file = open('input.txt','r')
lines = file.readlines()

total=0
for line in lines:
    numbers = [int(n)  for n in line.split(' ')]
    structure = [numbers]

    index=1
    while True:
        structure.append([])
        if len(structure[index-1])==1:
            structure[index].append(0)
        else:
            for i in range(0,len(structure[index-1])-1):
                structure[index].append(structure[index-1][i+1]-structure[index-1][i])

        if structure[index].count(0)==len(structure[index]):
            break;
        index+=1

    new_element_value=0
    for s in  reversed(structure):
        new_element_value=s[0]-new_element_value

    total+=new_element_value

print(f'The sum of extrapolated values is: {total}')
file.close()