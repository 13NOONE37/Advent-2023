file = open('input.txt','r')
lines = [list(line) for line in file.read().split('\n')]

WIDTH = len(lines[0])
HEIGHT = len(lines)

NORTH_OPTIONS=['|', 'F','7']
SOUTH_OPTIONS=['|', 'L','J']
WEST_OPTIONS=['-', 'F','L']
EAST_OPTIONS=['-', 'J','7']

def get_pipe(x,y):
    if 0<=x<=WIDTH-1 and 0<=y<=HEIGHT-1:
        return lines[y][x] 
    return None

def getNextPipe(prev_x,prev_y,x,y):   
    north=get_pipe(x,y-1)
    south=get_pipe(x,y+1)
    west=get_pipe(x-1,y)
    east=get_pipe(x+1,y)
    current = get_pipe(x,y)

    if current=='|':
        if prev_y<y and south:
            if south in SOUTH_OPTIONS:
                return x,y+1
        if prev_y>y and north:
            if north in NORTH_OPTIONS:
                return x,y-1
            
    if current=='-':
        if prev_x<x and east:
            if east in EAST_OPTIONS:
                return x+1,y
        if prev_x>x and west:
            if west in WEST_OPTIONS:
                return x-1,y
            
    if current=='L':
        if prev_y<y and east:
            if east in EAST_OPTIONS:
                return x+1,y
        if prev_x>x and north:
            if north in NORTH_OPTIONS:
                return x,y-1
            
    if current=='J':
        if prev_y<y and west:
            if west in WEST_OPTIONS:
                return x-1,y
        if prev_x<x and north:
            if north in NORTH_OPTIONS:
                return x,y-1
            
    if current=='7':
        if prev_y>y and west:
            if west in WEST_OPTIONS:
                return x-1,y
        if prev_x<x and south:
            if south in SOUTH_OPTIONS:
                return x,y+1
            
    if current=='F':
        if prev_y>y and east:
            if east in EAST_OPTIONS:
                return x+1,y
        if prev_x>x and south:
            if south in SOUTH_OPTIONS:
                return x,y+1
    
    return None


START_POS = [0,0]
POS = [0,0]
PREV_POS = [0,0]

for i in range(0,HEIGHT):
    if 'S' in lines[i]:
        x = lines[i].index('S')
        y = i

        START_POS[0] =  x
        START_POS[1] =  y
        north=get_pipe(x,y-1)
        south=get_pipe(x,y+1)
        west=get_pipe(x-1,y)
        east=get_pipe(x+1,y)

        if north in NORTH_OPTIONS and south in SOUTH_OPTIONS:
            lines[x][y]='|'
            PREV_POS[0] = POS[0]=x
            PREV_POS[1]=y-1
            POS[1] = y+1

        elif west in WEST_OPTIONS and east in EAST_OPTIONS:
            lines[x][y]='-'
            PREV_POS[1] = POS[1]=y
            PREV_POS[0]=x-1
            POS[0] = x+1

        elif west in WEST_OPTIONS and south in SOUTH_OPTIONS:
            lines[x][y]='7'
            PREV_POS[0]=x-1
            PREV_POS[1]=y
            POS[0] = x
            POS[1] = y+1

        elif east in EAST_OPTIONS and south in SOUTH_OPTIONS:
            lines[x][y]='F'
            PREV_POS[0]=x+1
            PREV_POS[1]=y
            POS[0] = x
            POS[1] = y+1

        elif west in WEST_OPTIONS and north in NORTH_OPTIONS:
            lines[x][y]='J'
            PREV_POS[0]=x-1
            PREV_POS[1]=y
            POS[0] = x
            POS[1] = y-1
        
        elif east in EAST_OPTIONS and north in NORTH_OPTIONS:
            lines[x][y]='L'
            PREV_POS[0]=x+1
            PREV_POS[1]=y
            POS[0] = x
            POS[1] = y-1
       

index=0
while START_POS!=POS:
    NEW_POS = getNextPipe(PREV_POS[0],PREV_POS[1],POS[0],POS[1])
    if NEW_POS:
        PREV_POS[0]=POS[0]
        PREV_POS[1]=POS[1]

        POS[0]=NEW_POS[0]
        POS[1]=NEW_POS[1] 

        index+=1
        continue
    break
    


index//=2
index+=1
print(f'Farthest position: {index}')
file.close()