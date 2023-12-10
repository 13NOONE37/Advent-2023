file = open('test.txt','r')
lines = file.readlines()

instructions = list(lines[0].strip())
nodes = {}
starting_nodes = []
for line in lines[2:]:
    name, tunells = line.split(' = ')
    name=name.strip()
    tunells=tunells[1:9].split(', ')

    nodes[name] = tunells
    if name[2]=='A':
        starting_nodes.append(name)

steps=0
index=0
increment=1
print(len(nodes),len(starting_nodes))


#idea: remove dups from starting_nodes and increment increment variabl
#!We need to find when will all ghosts met and then look for a tunnel
#!LCM is some kind of solution but we need to figure out how implement it
while True:
    # print(steps)
    steps+=increment
    break_all=True
    for i in range(0,len(starting_nodes)):
        node = starting_nodes[i]
        if instructions[index]=='R':
            new_node = nodes[node][1]

            starting_nodes[i]=new_node
            if new_node[2]!='Z':
                break_all=False
        else:                    
            new_node = nodes[node][0]
            starting_nodes[i]=new_node
            if new_node[2]!='Z':
                break_all=False

    print(starting_nodes)
    # length_diff = len(starting_nodes) - len(set(starting_nodes))
    # if length_diff>0:
    #     print('Shortening, length=',len(starting_nodes))
    #     starting_nodes = list(set(starting_nodes))
    #     increment+=length_diff

        
    if break_all: break
    index=(index+1)%len(instructions)

print(f'Reached ZZZ with {steps} steps')
file.close()