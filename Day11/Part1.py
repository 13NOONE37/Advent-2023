file = open('input.txt','r')

galaxy_map = [list(line) for line in file.read().split('\n')]

#double columns
column_index=0
while column_index<len(galaxy_map[0]):
    doubleColumn=True
    for row in galaxy_map:
        if row[column_index]!='.':
            doubleColumn=False
    if doubleColumn:
        for y in range(0,len(galaxy_map)):
            galaxy_map[y].insert(column_index+1,'.')
        column_index+=2
        continue
    column_index+=1

#double rows
row_index=0
while row_index<len(galaxy_map):
    row = galaxy_map[row_index]
    if  row.count('.')==len(row):
        galaxy_map.insert(row_index+1,row)
        row_index+=2
        continue
    row_index+=1


galaxy_coords = {}
galaxy_ids = []
galaxy_index=1
#numerate
for y in range(0,len(galaxy_map)):
    for x in range(0,len(galaxy_map[y])):
        if galaxy_map[y][x]=='#':
            galaxy_ids.append(galaxy_index)
            galaxy_coords[galaxy_index]=(x,y)
            galaxy_index+=1


#make pairs
pairs = [(galaxy_ids[i], galaxy_ids[j]) for i in range(len(galaxy_ids)) for j in range(i + 1, len(galaxy_ids))]


total=0
for pair in pairs:
    x_diff = abs(galaxy_coords[pair[0]][0] - galaxy_coords[pair[1]][0])
    y_diff = abs(galaxy_coords[pair[0]][1] - galaxy_coords[pair[1]][1])

    total+=x_diff+y_diff

print(f'Total is equal to {total}')
file.close()