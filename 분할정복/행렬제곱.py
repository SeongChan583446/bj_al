import sys
input = sys.stdin.readline

def mul(a,b):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    
    for i in range(n):
        for j in range(n):
            result[i][j] %= 1000

    return result

n,b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

b = bin(b)[2:]

result = [[1 if i==j else 0 for i in range(n)] for j in range(n)]

for i in range(len(b)):
    if b[-i-1] == '1':
        tmp = arr
        for j in range(i):
            tmp = mul(tmp,tmp)
        result = mul(result,tmp)

for i in result:
    print(*i)