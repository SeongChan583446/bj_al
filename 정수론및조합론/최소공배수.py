import sys
input = sys.stdin.readline

def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

t = int(input())
for i in range(t):
    x,y = map(int,input().split(' '))
    res = gcd(x,y)
    print(int((x*y)/res))