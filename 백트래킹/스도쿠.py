import sys
arr = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(9)]
zero_pos = [(i,j) for i in range(9) for j in range(9) if arr[i][j] == 0]

def possible(x,y):
    global arr
    poss_num = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        if arr[x][i] in poss_num:
            poss_num.remove(arr[x][i])
        if arr[i][y] in poss_num:
            poss_num.remove(arr[i][y])
    
    x //= 3
    y //= 3
    for i in range(3*x,3*(x+1)):
        for j in range(3*y,3*(y+1)):
            if arr[i][j] in poss_num:
                poss_num.remove(arr[i][j])

    return poss_num
flag = False
def dfs(n):
    global flag
    if flag:
        return
    
    if n == len(zero_pos):
        for i in arr:
            for j in i:
                print(j,end = ' ')
            print()
        flag = True
        return
    else:
        (i,j) = zero_pos[n]
        tmp = possible(i,j)
        for k in tmp:
            arr[i][j] = k
            dfs(n+1)
            arr[i][j] = 0

dfs(0)