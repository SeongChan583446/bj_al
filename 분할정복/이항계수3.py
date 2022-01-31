import sys
input = sys.stdin.readline

def power(num_a,num_b,num_c):
    if num_b == 0:
        return 1
    if num_b % 2 == 1:
        return (power(num_a,num_b//2,num_c) ** 2 * num_a) % num_c
    else:
        return (power(num_a,num_b//2, num_c) ** 2) % num_c
num = 1000000007
n,k = map(int,input().split())

fact = [1 for _ in range(n+1)]
for i in range(2,n+1):
    fact[i] = (fact[i-1] * i) % num

numerator = fact[n]
denominator = (fact[n-k] * fact[k]) % num

print(((numerator % num) * (power(denominator, num-2, num) % num)) % num)