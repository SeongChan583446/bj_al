import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    arr = deque(list(map(int,input().split())))
    if n == 1:
        print(1)
    else:
        count = 1
        idx = m
        while arr:
            if max(arr) == arr[0]:
                if idx == 0:
                    print(count)
                    break
                else:
                    arr.popleft()
                    count += 1
                    idx -= 1
            else:
                arr.append(arr.popleft())
                if idx == 0:
                    idx = len(arr)-1
                else:
                    idx -= 1