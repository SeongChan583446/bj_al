t = int(input())
h = []
w = []
n = []
for i in range(t):
    a, b, c = input().split(' ')
    h.append(int(a))
    w.append(int(b))
    n.append(int(c))

for i in range(t):
    if n[i]%h[i] == 0:
        print(h[i]*100 + int(n[i]/h[i]))
    else:
        print(n[i]%h[i] * 100 + int(n[i]/h[i]) + 1)