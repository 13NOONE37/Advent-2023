file = open('input.txt','r')

time_line = file.readline().split(':')[1].strip()
times = []
for time in time_line.split(' '):
    if time:
        times.append(int(time))

distance_line = file.readline().split(':')[1].strip()
distances = []
for distance in distance_line.split(' '):
    if distance:
        distances.append(int(distance))

ways = 1
for i in range(0,len(times)):
    time = times[i]
    distance = distances[i]
    ways_to_beat =0
    for m in range(0,time+1):
        veloctity = m
        time_left = time-m
        distance_traveled=veloctity*time_left
        
        if distance_traveled>distance:
            ways_to_beat+=1
    if ways_to_beat>0:
        ways*=ways_to_beat
print(f'There are {ways} to beat the all records')
