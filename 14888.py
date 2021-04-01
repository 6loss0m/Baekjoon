def dfs(i, current):
    global arr, op, result
    
    #print(i, current)
    if i == n-1:
        result.append(current)
        return
    else:
        # +
        if op[0] > 0:
            op[0] -= 1
            dfs(i+1, current + arr[i+1])
            op[0] += 1
        # -
        if op[1] > 0:
            op[1] -= 1
            dfs(i+1, current - arr[i+1])
            op[1] += 1
        # x
        if op[2] > 0:
            op[2] -= 1
            dfs(i+1, current * arr[i+1])
            op[2] += 1
        # /
        if op[3] > 0:
            op[3] -= 1
            if current < 0:
                dfs(i+1, -1 * (abs(current) // arr[i+1]))
            else:
                dfs(i+1, current // arr[i+1])
            op[3] += 1

n = int(input())
arr = list(map(int, input().split(' ')))
op = list(map(int, input().split(' ')))

result = []

dfs(0, arr[0])
#print(result)
print(max(result))
print(min(result))
