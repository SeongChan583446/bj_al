import sys
input = sys.stdin.readline

count = int(input())
arr_count = list(map(int,input().split(' ')))

print(max(arr_count)*min(arr_count))