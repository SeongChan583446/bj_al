import sys
input = sys.stdin.readline

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

n,k = map(int,input().split(' '))
res = fact(n)//(fact(k)*fact(n-k))
print(res % 10007)