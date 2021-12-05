m = int(input())
n = int(input())
sum = 0
minNum = n+1

for i in range(m,n+1):
    flag = 0
    if i != 1:
        for j in range(2,i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            if minNum > i:
                minNum = i
            sum += i

if sum == 0:
    print('-1')
else:
    print(sum)
    print(minNum)