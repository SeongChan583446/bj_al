import sys
input = sys.stdin.readline

def divide(x,y,n):
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]:
                print("(",end="")
                divide(x,y,n//2)
                divide(x,y+n//2,n//2)
                divide(x+n//2,y,n//2)
                divide(x+n//2,y+n//2,n//2)
                print(")",end="")
                return
    print(color,end="")

n = int(input())
arr = [list(map(int,input().rstrip())) for _ in range(n)]

divide(0,0,n)