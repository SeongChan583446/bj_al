import sys
input = sys.stdin.readline

n = int(input())
load_len = list(map(int,input().split(' ')))
cpl = list(map(int,input().split(' ')))

res = cpl[0] * load_len[0]
cur_cpl = cpl[0]

if n>2:
    for i in range(1,n-1):
        if cur_cpl > cpl[i]:
            cur_cpl = cpl[i]
        res += cur_cpl * load_len[i]

print(res)