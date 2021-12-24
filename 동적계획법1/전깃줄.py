import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split(' '))))

arr.sort()
tmp = []
for i in range(n):
    tmp.append(arr[i][1])

res = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if tmp[i] > tmp[j] and res[i] < res[j]:
            res[i] = res[j]
    res[i] += 1

print(n-max(res))