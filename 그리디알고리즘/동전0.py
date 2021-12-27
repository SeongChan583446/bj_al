import sys
input = sys.stdin.readline

n,k = map(int,input().split(' '))
coin = []
count = 0
for i in range(n):
    coin.append(int(input()))

coin.reverse()

for i in coin:
    if k//i != 0:
        count += k//i
        k -= (k//i) * i

print(count)