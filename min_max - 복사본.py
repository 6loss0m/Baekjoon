n = input()
ar = list(map(int, input().split()))
max = min = ar[0]

for i in ar:
    if max < i:
        max = i
    if min > i:
        min = i
print(min,max)
    
