x,y,z = map(int,input().split(' '))
while(not(x == 0 and y == 0 and z == 0)):
    arr = []
    arr.append(x)
    arr.append(y)
    arr.append(z)
    tmp = max(arr)
    arr.remove(tmp)
    if arr[0]**2 + arr[1]**2 == tmp**2:
        print("right")
    else:
        print("wrong")
    x,y,z = map(int,input().split(' '))