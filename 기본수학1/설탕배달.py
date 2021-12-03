n = int(input())
n3 = 0
n5 = 0
min = 2000
for i in range(int(n/3)+1):
    if (n - 3*i)%5 == 0:
        n3 = i
        n5 = int((n-3*i) / 5)
        if n3+n5 < min:
            min = n3+n5

if min == 2000 :
    print("-1")
else:
    print(min)