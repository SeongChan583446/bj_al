import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    sum = 0
    vps = list(input())
    for j in vps:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
    
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")