n = int(input())
x = input()
count = 0
for i in range(n):
    flag = 0
    tmp = int(x.split(' ')[i])
    if tmp != 1:
        for j in range(2,tmp):
            if tmp % j == 0:
                flag = 1
        if flag == 0:
            count += 1

print(count)