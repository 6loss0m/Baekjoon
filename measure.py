p, k= map(int, input().split())

cnt = 0
for i in range(1,p+1):
    if p%i == 0:
        cnt = cnt + 1
    if cnt == k :
        print(i)
        break
if(cnt < k):
    print(0)
