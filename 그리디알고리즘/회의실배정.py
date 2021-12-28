import sys
input = sys.stdin.readline

n = int(input())
arr = []
comp = [0 for _ in range(n)]
for i in range(n):
    arr.append(list(map(int,input().split(' '))))

arr.sort()
arr.sort(key = lambda x:x[1])

count = 0
last_end = 0
for start, end in arr:
    if start >= last_end:
        count += 1
        last_end = end
print(count)