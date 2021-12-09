n = input()
arr = []
for i in range(len(n)):
    arr.append(int(n[i]))
arr.sort()
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end='')