def find(num):
    flag = 0
    for i in range(2,num):
        if num % i == 0:
            flag = 1
            break
    return flag #0이면 소수 1이면 그외

n = int(input())
arr = []
if n != 1:
    tmp = n
    while(find(tmp) != 0):
        for i in range(2,tmp):
            if tmp%i==0 and find(i)==0:
                tmp = int(tmp/i)
                arr.append(i)
                break
    arr.append(tmp)

for i in arr:
    print(i)