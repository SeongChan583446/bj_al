t = int(input())
k = []
n = []
arr = []
for i in range(t):
    a = int(input())
    b = int(input())
    k.append(int(a))
    n.append(int(b))

for i in range(t):
    for j in range(k[i] + 1):
        tmp = []
        for l in range(n[i]):
            if j==0:
                tmp.append(l+1)
            else:
                sum = 0
                for m in range(l+1):
                    sum += arr[m]
                tmp.append(sum)
        arr = tmp
    print(tmp[-1])