import sys
n = int(input())
arr = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().split(' '))
    tmp = []
    tmp.append(x)
    tmp.append(y)
    arr.append(tmp)

arr.sort()
for i in arr:
    for j in i:
        print(j,end=' ')
    print()