n = int(input())
temp = 1
count = 1

while(temp < n):
    temp += 6*count
    count += 1

print(count)