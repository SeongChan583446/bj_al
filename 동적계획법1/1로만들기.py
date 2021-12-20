import sys
input = sys.stdin.readline

n = int(input())

arr = [0]*(n+1)
if n == 1:
    print(0)
elif n == 2 or n == 3:
    print(1)
else:
    arr[1] = 0
    arr[2] = 1
    arr[3] = 1
    for i in range(4,n+1):
        if i%2 == 0 and i%3 == 0:
            arr[i] = min(arr[i//3],arr[i//2],arr[i-1]) + 1
        elif i%3 == 0:
            arr[i] = min(arr[i//3],arr[i-1]) + 1
        elif i%2 == 0:
            arr[i] = min(arr[i//2],arr[i-1]) + 1
        else:
            arr[i] = arr[i-1] + 1

    print(arr[-1])