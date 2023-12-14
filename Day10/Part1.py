file = open('test.txt','r')
lines = [list(line) for line in file.read().split('\n')]
# print(lines)

WIDTH = len(lines[0])
HEIGHT = len(lines)


def get_pipe(x,y):
    if 0<x<WIDTH-1 or 0<y<HEIGHT-1:
        return lines[x][y] 
    return None

def getNextPipe(prev_x,prev_y,x,y,forcedPipe=None):      
    top=get_pipe(x,y-1)
    bottom=get_pipe(x,y+1)
    left=get_pipe(x-1,y)
    right=get_pipe(x+1,y)
    current = get_pipe(x,y)
    if forcedPipe:
        current=forcedPipe

    if not current: return None

    if current=='|':
        if prev_y<=y and bottom:
            #we are coming from north
            #south solutions
            if bottom in ('|', 'L', 'J'):
                return x,y+1
        if prev_y>=y and top:
            #we are coming from south
            #north solutions
            if top in ('|', 'F', '7'):
                return x,y-1
            
    if current=='-':
        if prev_x<=x and right:
            #we are coming from west
            #east solutions
            if right in ('-', '7', 'J'):
                return x+1,y
        if prev_x>=x and left:
            #we are coming from east
            #west solutions
            if left in ('-', 'F', 'L'):
                return x-1,y
            
    if current=='L':
        if prev_y<=y and right:
            #We are coming from north
            #east solutions
            if top in ('-', 'J', '7'):
                return x+1,y
        if prev_x>=x and top:
            #We are coming from east
            #north solutions
            if top in ('|', 'F', '7'):
                return x,y-1
            
    if current=='J':
        if prev_y<=y and left:
            #We are coming from north
            #west solutions
            if top in ('-', 'F', 'L'):
                return x-1,y
        if prev_x>=x and top:
            #We are coming from west
            #north solutions
            if top in ('|', 'F', '7'):
                return x,y-1
            
    if current=='7':
        if prev_y>=y and left:
            #We are coming from south
            #west solutions
            if left in ('-', 'L', 'F'):
                return x-1,y
        if prev_x<=x and bottom:
            #We are coming from west
            #south solutions
            if bottom in ('|', 'J', 'L'):
                return x,y-1
            
    if current=='F':
        if prev_y>=y and right:
            #We are coming from south
            #east solutions
            if right in ('-', '7', 'J'):
                return x+1,y
        if prev_x>=x and bottom:
            #We are coming from east
            #south solutions
            if bottom in ('|', 'J', 'L'):
                return x,y+1
    
    return None
    
START_POS = [0,0]
POS = [0,0]
PREV_POS = [0,0]

for i in range(0,HEIGHT):
    if 'S' in lines[i]:
        x = lines[i].index('S')
        y = i

        #!!Replace  S with coresponding pipe type
        #!!Tempoary solution
        # print(x,y)
        # print(getNextPipe(x,y,x,y,'|'))
        # getNextPipe(x,y)
        lines[x][y]='F'
        START_POS[0]=0
        START_POS[1]=2
        PREV_POS[0]=0
        PREV_POS[1]=2
        POS[0]=1
        POS[1]=2
        # START_POS[0] = PREV_POS[0] = POS[0] = x
        # START_POS[1] = PREV_POS[1] = POS[1] = y
        break;


#replace char with coresponding

#update POS_UP and POS_DOWN
index=0
while START_POS!=POS:
    NEW_POS = getNextPipe(PREV_POS[0],PREV_POS[1],POS[0],POS[1])
    print(NEW_POS)
    if NEW_POS:
        PREV_POS[0]=POS[0]
        PREV_POS[1]=POS[1]

        POS[0]=NEW_POS[0]
        POS[1]=NEW_POS[1] 

        index+=1
        continue
    break
    



print(f'Farthest position: {index}')
file.close()