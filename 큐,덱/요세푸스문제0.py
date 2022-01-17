import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
arr = deque([i+1 for i in range(n)])

print('<',end='')
while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    print(arr.popleft(),end="")
    if arr:
        print(", ",end="")

print('>')