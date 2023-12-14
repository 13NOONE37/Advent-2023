file = open('input.txt','r')

galaxy_map = [list(line) for line in file.read().split('\n')]

#double columns
column_index=0
columns_duplicates_ids=[]
while column_index<len(galaxy_map[0]):
    doubleColumn=True
    for row in galaxy_map:
        if row[column_index]!='.':
            doubleColumn=False
    if doubleColumn:
        columns_duplicates_ids.append(column_index)
    column_index+=1

#double rows
row_index=0
rows_duplicates_ids=[]

while row_index<len(galaxy_map):
    row = galaxy_map[row_index]
    if  row.count('.')==len(row):
        rows_duplicates_ids.append(row_index)
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
multiplier=1000000
for pair in pairs:
    min_x = min(galaxy_coords[pair[0]][0], galaxy_coords[pair[1]][0])
    max_x = max(galaxy_coords[pair[0]][0], galaxy_coords[pair[1]][0])
    min_y = min(galaxy_coords[pair[0]][1], galaxy_coords[pair[1]][1])
    max_y = max(galaxy_coords[pair[0]][1], galaxy_coords[pair[1]][1])
   
    x_diff = max_x-min_x
    y_diff = max_y-min_y

    for index in columns_duplicates_ids:
        if min_x < index <= max_x:
            x_diff+=multiplier-1

    for index in rows_duplicates_ids:
        if min_y < index <= max_y:
            y_diff+=multiplier-1
            
    total+=x_diff+y_diff

print(f'Total is equal to {total}')
file.close()