import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
res = [0]*(n+1)
for i in range(n):
    arr.append(int(input()))

res[1] = arr[1]
res[2] = arr[1]+arr[2]
res[3] = max(arr[1],arr[2])+arr[3]
for i in range(4,n+1):
    res[i] = max(arr[i-1]+res[i-3],res[i-2])+arr[i]

print(res[-1])