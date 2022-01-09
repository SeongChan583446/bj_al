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
            print("N0")
            break
    
    if sum == 0:
        print("YES")
    else:
        print("NO")