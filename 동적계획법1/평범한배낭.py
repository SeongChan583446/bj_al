import sys
input = sys.stdin.readline

n,k = map(int,input().split(' '))
arr = []
res = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n):
    tmp = list(map(int,input().split(' ')))
    arr.append(tmp)

for i in range(1,n+1):
    for j in range(1,k+1):
        w = arr[i-1][0]
        v = arr[i-1][1]

        if j < w:
            res[i][j] = res[i][j-1]
        else:
            res[i][j] = max(res[i-1][j],res[i-1][j-w]+v)

print(max(res[-1]))