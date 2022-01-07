import sys
input = sys.stdin.readline

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

n = int(input())
res = fact(n)
count = 0
while True:
    if res % 10 != 0:
        break
    res //= 10
    count += 1

print(count)