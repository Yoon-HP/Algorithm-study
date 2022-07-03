from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
Map=[list(map(int,input().split())) for _ in range(N)]
Map_cnt=[0]*(101)
h=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
while h<=100:
    cnt=0
    check=[[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Map[i][j]<=h:
                check[i][j]=True
                
    for i in range(N):
        for j in range(N):
            if not check[i][j]:
                q=deque([[i,j]])
                check[i][j]=True
                while q:
                    u,v=q.popleft()
                    for k in range(4):
                        a=u+dx[k]
                        b=v+dy[k]
                        if 0<=a<N and 0<=b<N and not check[a][b]:
                            q.append([a,b])
                            check[a][b]=True
                cnt+=1
                
    Map_cnt[h]=cnt
    h+=1
print(max(Map_cnt))