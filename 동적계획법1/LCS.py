import sys
input = sys.stdin.readline

str1 = input().strip().upper()
str2 = input().strip().upper()
len1 = len(str1)
len2 = len(str2)
arr = [[0 for _ in range(len2+1)] for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if str1[i-1] == str2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j],arr[i][j-1])

print(arr[-1][-1])