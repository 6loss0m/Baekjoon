train = [list(map(int,input().split())) for i in range(0,10)]
people = 0
max = train[0][1]
for i in train :
    people = people - i[0]
    people = people + i[1]
    if max < people :
        max = people
print(max)
    
