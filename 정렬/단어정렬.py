import sys
n = int(input())
arr = []
for i in range(51):
    arr.append([])

for i in range(n):
    tmp = sys.stdin.readline()
    if not (tmp[:-1] in arr[len(tmp)-1]):
        arr[len(tmp)-1].append(tmp[:-1])

for i in arr:
    if len(i) != 0:
        i.sort()
        for j in i:
            print(j)