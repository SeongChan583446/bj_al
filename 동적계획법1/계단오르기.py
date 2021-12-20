import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*301
res = [0]*301
for i in range(n):
    arr[i] = int(input())

res[0] = arr[0]
res[1] = arr[0]+arr[1]
res[2] = max(arr[1]+arr[2],arr[0]+arr[2])
for i in range(3,n):
    res[i] = max(arr[i-1]+res[i-3],res[i-2])+arr[i]

print(res[n-1])