import sys
input = sys.stdin.readline

def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

tmp = []
for i in range(n-1):
    tmp.append(arr[i+1]-arr[i])

prev_gcd = tmp[0]
for i in range(1,len(tmp)):
    prev_gcd = gcd(prev_gcd,tmp[i])

res = []
for i in range(2,int(prev_gcd**0.5)+1):
    if prev_gcd%i == 0:
        res.append(i)
        res.append(prev_gcd//i)
res.append(prev_gcd)
res = list(set(res))
res.sort()
print(*res)