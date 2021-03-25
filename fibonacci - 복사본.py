fibo = []
fibo.append(0)
fibo.append(1)
n = int(input())
if n == 0:
    print(fibo[0])
elif n == 1:
    print(fibo[1])
else:
    for i in range(2,21):
        fibo.append(fibo[i-1] + fibo[i-2])
        if len(fibo)-1 == n:
            print(fibo[i])
            break    
