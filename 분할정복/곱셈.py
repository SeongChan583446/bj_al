import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

def power(num_a,num_b,num_c):
    if num_b == 1:
        return num_a%num_c
    else:
        tmp = power(num_a,num_b//2,num_c)
        if num_b % 2 == 0:
            return (tmp * tmp) % num_c
        else:
            return (tmp * tmp * num_a) % num_c

print(power(a,b,c))