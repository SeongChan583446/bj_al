import sys
n = int(input())
arr = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().split(' '))
    tmp = []
    tmp.append(y)
    tmp.append(x)
    arr.append(tmp)

arr.sort()
for i in arr:
    for j in range(1,-1,-1):
        print(i[j],end=' ')
    print()