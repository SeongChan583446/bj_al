n = int(input())

count = 1

while(n > count):
    n-=count
    count+=1

if count%2 == 1:
    print(str(count+1-n) + '/' + str(n))
else:
    print(str(n) + '/' + str(count+1-n))