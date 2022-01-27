import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
result = [0,0,0]

def divide(x,y,n):
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            tmp = n//3
            if color != arr[i][j]:
                divide(x,y,tmp)
                divide(x,y+tmp,tmp)
                divide(x,y+2*tmp,tmp)
                divide(x+tmp,y,tmp)
                divide(x+tmp,y+tmp,tmp)
                divide(x+tmp,y+2*tmp,tmp)
                divide(x+2*tmp,y,tmp)
                divide(x+2*tmp,y+tmp,tmp)
                divide(x+2*tmp,y+2*tmp,tmp)
                return
    if color == -1:
        result[0] += 1
    elif color == 0:
        result[1] += 1
    else:
        result[2] += 1

divide(0,0,n)
print(result[0])
print(result[1])
print(result[2])