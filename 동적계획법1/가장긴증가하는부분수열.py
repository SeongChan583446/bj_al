n = int(input())
arr = list(map(int,input().split(' ')))
res = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and res[i] < res[j]:
            res[i] = res[j]
    res[i] += 1

print(max(res))