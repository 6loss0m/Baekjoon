ar = [int(input()) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if sum(ar) - ar[i] - ar[j] == 100:
            remove = [ar[i],ar[j]]

ar.remove(remove[0])
ar.remove(remove[1])
ar.sort()
for i in ar:
    print(i)
