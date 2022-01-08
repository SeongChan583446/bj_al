import sys
input = sys.stdin.readline

k = int(input())
arr = []
for i in range(k):
    command = int(input())
    if command != 0:
        arr.append(command)
    else:
        arr.pop()

print(sum(arr))