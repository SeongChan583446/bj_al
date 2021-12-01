x, y, z = input().split(' ')
a = int(x)
b = int(y)
c = int(z)
if b >= c:
    print("-1")
else:
    print(int(a / (c - b) + 1))