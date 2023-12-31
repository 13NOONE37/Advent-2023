file = open('input.txt','r')

blocks = file.read().split('\n\n')

seeds_line = ''.join(blocks[0].split(':')[1]).strip().split(' ')
seeds = []
for seed in seeds_line:
    seeds.append(int(seed))

lowest_location = -1
for seed in seeds:
    for line in blocks[1:]:
        instructions = line.split('\n')[1:]
        for instruction in instructions:
            destination_start,source_start,range_length = [int(num) for num in instruction.split(' ')]
            diff = source_start-destination_start
            if source_start <= seed <=source_start+range_length:
                seed-=diff
                break;
           
    if lowest_location==-1 or seed<lowest_location:
        lowest_location=seed


print(f'The lowest location of seed is {lowest_location}')