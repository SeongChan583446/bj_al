import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    dict = {}
    sum = 1
    n = int(input())
    for j in range(n):
        name, kind = input().split(' ')
        kind = kind[:-1]
        if kind in dict:
            dict[kind] += 1
        else:
            dict[kind] = 1

    for k in dict:
        sum *= dict[k]+1
    sum -= 1

    print(sum)