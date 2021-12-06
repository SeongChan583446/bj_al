def find(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

arr = []

for i in range(2,246912):
    if find(i):
        arr.append(i)

n = int(input())

while(True):
    count = 0
    if n==0:
        break
    for i in arr:
        if n<i<=2*n:
            count+=1
    print(count)
    n = int(input())