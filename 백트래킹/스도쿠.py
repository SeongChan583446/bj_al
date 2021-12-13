import sys
arr = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(9)]
zero_pos = [(i,j) for i in range(9) for j in range(9) if arr[i][j] == 0]

def possible(x,y):
    global arr
    poss_num = [i+1 for i in range(9)]
    for i in range(9):
        if arr[x][i] in poss_num:
            poss_num.remove(arr[x][i])
        if arr[i][y] in poss_num:
            poss_num.remove(arr[i][y])
    
    x //= 3 #0-2 : 0 / 3-5 : 1 / 6-8 : 2
    y //= 3
    for i in range(3*x,3*(x+1)):
        for j in range(3*y,3*(y+1)):
            if arr[i][j] in poss_num:
                poss_num.remove(arr[i][j])

    return poss_num

def dfs(n):
    global arr
    if n > len(zero_pos):
        return
    
    if n == len(zero_pos):
        for i in arr:
            for j in i:
                print(j,end = ' ')
            print()
        return
    else:
        (i,j) = zero_pos[n]
        tmp = possible(i,j)
        for k in tmp:
            arr[i][j] = k
            dfs(n+1)
            arr[i][j] = 0



dfs(0)