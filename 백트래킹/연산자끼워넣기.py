import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split(' ')))
ops = list(map(int,input().split(' ')))
maxNum = -1e9
minNum = 1e9

def dfs(count, tmpresult, plus, minus, multiple, divide):
    global minNum, maxNum, n
    if count == n-1:
        minNum = min(tmpresult,minNum)
        maxNum = max(tmpresult,maxNum)
        return
    
    if plus > 0:
        dfs(count + 1, tmpresult + nums[count+1], plus - 1, minus, multiple, divide)
    if minus > 0:
        dfs(count + 1, tmpresult - nums[count+1], plus, minus - 1, multiple, divide)
    if multiple > 0:
        dfs(count + 1, tmpresult * nums[count+1], plus, minus, multiple - 1, divide)
    if divide > 0:
        dfs(count + 1, int(tmpresult / nums[count+1]), plus, minus, multiple, divide - 1)

dfs(0, nums[0], ops[0], ops[1], ops[2], ops[3])
print(maxNum)
print(minNum)