import sys
input = sys.stdin.readline

def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

x,y = map(int,input().split(' '))
res_gcd = gcd(x,y)

print(res_gcd)
print(int((x*y)/res_gcd))