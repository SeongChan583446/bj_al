import sys
input = sys.stdin.readline

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

t = int(input())

for i in range(t):
    n,k = map(int,input().split(' '))
    if k>n:
        tmp = k
        k = n
        n = tmp
    print(fact(n)//(fact(k)*fact(n-k)))