def find(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

t = int(input())
for i in range(t):
    a = 0
    b = 0
    n = int(input())
    for j in range(n//2,1,-1):
        if find(j) and find(n-j):
            print(j,n-j)
            break