import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split(' '))) for _ in range(n)]
member_arr = [i for i in range(n)]
teams = list(combinations(member_arr, n//2))

minNum = 2000

for i in range(len(teams)//2):
    team_A = teams[i]
    sum_A = 0
    for j in range(n//2):
        member = team_A[j]
        for k in team_A:
            sum_A += s[member][k]

    team_B = teams[-i-1]
    sum_B = 0
    for j in range(n//2):
        member = team_B[j]
        for k in team_B:
            sum_B += s[member][k]

    minNum = min(minNum,abs(sum_A - sum_B))

print(minNum)