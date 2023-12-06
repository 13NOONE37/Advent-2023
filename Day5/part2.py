file = open('test.txt','r')
blocks = file.read().split('\n\n')

seeds_line = ''.join(blocks[0].split(':')[1]).strip().split(' ')
seeds = []
for i in range(0,len(seeds_line),2):
    seed_value = int(seeds_line[i])
    seed_range = int(seeds_line[i+1])
    seeds.append((seed_value,seed_value+seed_range))

procedures = []
for line in blocks[1:]:
    instructions = line.split('\n')[1:]
    procedure = []

    for instruction in instructions:
        destination_start,source_start,range_length = [int(num) for num in instruction.split(' ')]
        diff = source_start-destination_start
        procedure.append((source_start,source_start+range_length, diff))
    procedures.append(procedure)


lowest_location = -1
for seed in seeds:
    local_seed=seed[0]
    for procedure in procedures:
        print('⭕Procedure: ', procedure)
        for range_start,range_end, diff in procedure:
            print('🎭Iteration of proced local_seed is equal to', local_seed)
            # if diff>=0:
            #     local_seed=seed[0]
            # else:
            #     local_seed=seed[1]
            if local_seed!=0 and range_start <= local_seed <=range_end:
                local_seed-=diff
                break;
        
        if lowest_location==-1 or local_seed<lowest_location:
            lowest_location=local_seed
        print('💙after Iteration of proced local_seed is equal to', local_seed, ' for seed ', seed)
        



#plan optymalizacji
#po tym jak iterujemy w celu zdobycia nasion(bierzemy krotke z dwoma wartoścami) iterujemy w celu zdobycia zakresów pozostałych czynności zapisujemy je do zagnieżdzonej listy
# iterujemy po seeds i po kolei wykonujemy kolejne czyności z uwzględnieem pomysłu o najmniejszej i najwiekszej wartosci(albo i nie przemyslec)


print(f'The lowest location of seed is {lowest_location}')