file = open('input.txt','r')

time_line = file.readline().split(':')[1].strip()
time=''
for t in time_line.split(' '):
    if t:
        time+=t
time=int(time)

distance_line = file.readline().split(':')[1].strip()
distance=''
for d in distance_line.split(' '):
    if d:
        distance+=d
distance=int(distance)


ways_1=0
for i in range(time//2,-1,-1):
    veloctity = i
    time_left = time-i
    distance_traveled=veloctity*time_left
        
    if distance_traveled<=distance:
        ways_1=i
        break

ways_2 = 0
for i in range(time//2,time+1):
    veloctity = i
    time_left = time-i
    distance_traveled=veloctity*time_left
        
    if distance_traveled<=distance:
        ways_2=i-1
        break

print(f'There are {ways_2-ways_1} ways to beat the record')

#binary search would be a lot of better