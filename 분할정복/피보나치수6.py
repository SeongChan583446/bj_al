import sys
input = sys.stdin.readline

def power(n):
    arr = [[1,1],[1,0]]
    result = arr
    for i in range(n):
        result = [[0,0],[0,0]]
        for x in range(2):
            for y in range(2):
                for j in range(2):
                    result[x][y] += (arr[x][j] * arr[j][y]) % 1000000007
        arr = result

    return result

def mul(a,b):
    result = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (a[i][k] * b[k][j]) % 1000000007

    return result

n = int(input())

n = bin(n)[2:]
print('n',n)
result = [[1,0],[0,1]]

for i in range(len(n)):
    if n[-i-1] == '1':
        result = mul(result,power(i))
        print(result,i)

print(result[0][1] % 1000000007)