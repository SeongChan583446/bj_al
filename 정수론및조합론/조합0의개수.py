import sys
input = sys.stdin.readline

def find_two(n):
    count = 0
    while n != 0:
        n //= 2
        count += n
    return count

def find_five(n):
    count = 0
    while n != 0:
        n //= 5
        count += n
    return count

n,k = map(int,input().split(' '))

print(min(find_two(n)-(find_two(k)+find_two(n-k)),find_five(n)-(find_five(k)+find_five(n-k))))