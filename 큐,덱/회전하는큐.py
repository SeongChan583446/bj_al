import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

circle = deque([i+1 for i in range(n)])

count = 0
i = 0
while i != m:
    target = arr[i]
    if target == circle[0]:
        circle.popleft()
        i += 1
    else:
        target_position = circle.index(target)
        if target_position <= len(circle) // 2:
            for j in range(target_position):
                circle.append(circle.popleft())
                count += 1
        else:
            for j in range(len(circle)-target_position):
                circle.insert(0,circle.pop())
                count += 1
    
    print(count,circle)

print(count)