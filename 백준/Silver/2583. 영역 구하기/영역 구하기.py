from collections import deque
import sys
input=sys.stdin.readline
M,N,K=map(int,input().split())
Map=[[0]*(N) for _ in range(M)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            Map[i][j]=1

Area=[]
for i in range(M):
    for j in range(N):
        if Map[i][j]==0:
            A=0
            q=deque([[i,j]])
            Map[i][j]=1
            while q:
                u,v=q.popleft()
                A+=1
                for k in range(4):
                    a=u+dx[k]
                    b=v+dy[k]
                    if 0<=a<M and 0<=b<N:
                        if Map[a][b]==0:
                            q.append([a,b])
                            Map[a][b]=1

            Area.append(A)
print(len(Area))
Area.sort()
for i in Area:
    print(i,end=' ')