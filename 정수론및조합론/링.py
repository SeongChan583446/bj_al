import sys
input = sys.stdin.readline

def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

n = int(input())
arr = list(map(int,input().split(' ')))

for i in range(1,n):
    tmp_gcd = gcd(arr[0],arr[i])
    print("%d/%d" %(arr[0]//tmp_gcd, arr[i]//tmp_gcd))