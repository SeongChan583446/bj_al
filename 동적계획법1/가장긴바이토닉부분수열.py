n = int(input())
arr = list(map(int,input().split(' ')))
res = [0 for _ in range(n)]
tmp_inc = [0 for _ in range(n)]
tmp_dec = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and tmp_inc[i] < tmp_inc[j]:
            tmp_inc[i] = tmp_inc[j]
    tmp_inc[i] += 1

arr.reverse()
 
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and tmp_dec[i] < tmp_dec[j]:
            tmp_dec[i] = tmp_dec[j]
    tmp_dec[i] += 1

tmp_dec.reverse()
for i in range(n):
    res[i] = tmp_inc[i] + tmp_dec[i] - 1

print(max(res))