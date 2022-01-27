import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    error_flag = False
    count_reverse = 0
    func = input().rstrip()
    n = int(input())
    arr = deque(list(input().rstrip()[1:-1].split(",")))

    if n == 0:
        arr = []
    
    for j in func:
        if j == 'R':
            count_reverse += 1
        elif j == 'D':
            if len(arr) < 1:
                error_flag = True
                break
            else:
                if count_reverse % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    
    if error_flag == True:
        print("error")
    else:
        if count_reverse % 2 != 0:
            arr.reverse()
        print("["+",".join(arr)+"]")