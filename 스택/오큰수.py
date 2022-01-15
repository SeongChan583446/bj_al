import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr_s = []
arr_res = [-1 for _ in range(n)]

arr_s.append(0)
for i in range(1,n):
    while arr_s and arr[arr_s[-1]] < arr[i]:
        arr_res[arr_s.pop()] = arr[i]
    arr_s.append(i)

print(*arr_res)