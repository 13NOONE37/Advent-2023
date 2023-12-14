file = open('test.txt','r')
lines = file.readlines()

for line in lines:
    print(line)


file.close()