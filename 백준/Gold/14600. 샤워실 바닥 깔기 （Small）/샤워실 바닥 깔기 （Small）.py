K=int(input())
y,x=map(int,input().split())
x-=1;y-=1

def rotate_270(arr):
    n=len(arr)
    ret=[[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            ret[n-1-c][r]=arr[r][c]
    return ret

if K==1:
    result=[[1]*2**K for _ in range(2**K)]
    result[y][x]=-1
    result=rotate_270(result)
    for i in result:
        print(*i)

elif K==2:
    result=[[0]*2**K for _ in range(2**K)]
    for i in range(4):
        for j in range(4):
            if i<=1 and j<=1:
                result[j][i]=4
            elif i<=1 and j>=2:
                result[j][i]=1
            elif i>=2 and j<=1:
                result[j][i]=5
            else:
                result[j][i]=2
    x,y=(3-x),y
    if x<2 and y<2:
        result[x][y]=-1
        for i in range(1,3):
            for j in range(1,3):
                if i!=1 or j!=1:
                    result[i][j]=3
    elif x<2 and y>=2:
        result[x][y]=-1
        for i in range(1,3):
            for j in range(1,3):
                if i!=1 or j!=2:
                    result[i][j]=3
    elif x>=2 and y<2:
        result[x][y]=-1
        for i in range(1,3):
            for j in range(1,3):
                if i!=2 or j!=1:
                    result[i][j]=3
    else:
        result[x][y]=-1
        for i in range(1,3):
            for j in range(1,3):
                if i!=2 or j!=2:
                    result[i][j]=3      
    for i in result:
        print(*i)  