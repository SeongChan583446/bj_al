import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr_a = []
for i in range(n):
    arr_a.append(list(map(int,input().split())))

m,k = map(int,input().split())
arr_b = []
for i in range(m):
    arr_b.append(list(map(int,input().split())))

result = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j] += arr_a[i][l] * arr_b[l][j]

for i in range(n):
    for j in range(k):
        print(result[i][j],end=" ")
    print()