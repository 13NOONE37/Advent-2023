file = open('input.txt','r')
lines = file.readlines()

instructions = list(lines[0].strip())
nodes = {}
for line in lines[2:]:
    name, tunells = line.split(' = ')
    name=name.strip()
    tunells=tunells[1:9].split(', ')

    nodes[name] = tunells

steps=0
index=0
current_node='AAA'
while True:
    steps+=1
    if instructions[index]=='R':
        current_node=nodes[current_node][1]
    else:        
        current_node=nodes[current_node][0]

    if current_node=='ZZZ':
        break
    index=(index+1)%len(instructions)

print(f'Reached ZZZ with {steps} steps')
file.close()