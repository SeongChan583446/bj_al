import sys
n = int(input())
arr = []
for i in range(201):
    arr.append([])
for i in range(n):
    age,name = sys.stdin.readline().split(' ')
    age = int(age)
    arr[age].append(name[:-1])

print(arr)

for i in range(len(arr)):
    if len(arr[i]) != 0:
        for j in range(len(arr[i])):
            print(i,arr[i][j])