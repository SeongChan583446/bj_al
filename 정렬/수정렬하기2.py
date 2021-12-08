n = int(input())
arr = []
for i in range(n):
    tmp = int(input())
    arr.append(tmp)

arr.sort()
for i in arr:
    print(i)