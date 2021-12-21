import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for i in range(1,n+1):
    arr.append(int(input()))

res = [0]
res.append(arr[1])
if n>=2:
    res.append(arr[1]+arr[2])
if n>=3:
    for i in range(3,n+1):
        res.append(max(res[i-1],res[i-2]+arr[i],res[i-3]+arr[i-1]+arr[i]))

print(res[-1])
