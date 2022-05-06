import sys
input=sys.stdin.readline
T=int(input())
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def gogo(u,v,dir):
    while True:
        if [u,v,dir] not in check:
            u,v=u+dx[dir],v+dy[dir]
            if u==-1 or u==n or v==-1 or v==n:
                    return print(u+1,v+1)
            while Map[u][v]==0:
                u,v=u+dx[dir],v+dy[dir]
                if u==-1 or u==n or v==-1 or v==n:
                    return print(u+1,v+1)
            check.append([u,v,dir])
            if dir==0:
                dir=1
            elif dir==1:
                dir=2
            elif dir==2:
                dir=3
            else:
                dir=0
        else:
            return print(0,0)
            
                
        
for _ in range(T):
    n,r=map(int,input().split())
    Map=[[0 for _ in range(n)] for _ in range(n)]
    point=[]
    for i in range(r):
        a,b=map(int,input().split())
        Map[a-1][b-1]=1
    u,v=map(int,input().split())
    u-=1;v-=1
    if u==n:
        dir=3
    if u==-1:
        dir=1
    if v==-1:
        dir=0
    if v==n:
        dir=2
    check=[]
    gogo(u,v,dir)