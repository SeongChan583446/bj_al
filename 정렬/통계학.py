import sys
n = int(input())
arr = [0]*8001
arr2 = []
tmp_arr = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    arr[tmp+4000] += 1
    arr2.append(tmp)
maxNum = max(arr)

arr2.sort()
print(round(sum(arr2)/n))
print(arr2[n//2])
for i in range(8001):
    if maxNum == arr[i]:
        tmp_arr.append(i-4000)

if len(tmp_arr) == 1:
    print(tmp_arr[0])
else:
    print(tmp_arr[1])
print(max(arr2)-min(arr2))
