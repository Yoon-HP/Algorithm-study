# 2146번 다리 만들기
from collections import deque

N=int(input())
Map=[list(map(int,input().split())) for _ in range(N)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

visit=[[False]*N for _ in range(N)]
land=1
for i in range(N):
    for j in range(N):
        if Map[i][j]!=0 and not visit[i][j]:
            q=deque([[i,j]])
            visit[i][j]=True
            Map[i][j]=land
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if nx<0 or nx>=N or ny<0 or ny>=N:
                        continue
                    if visit[nx][ny]:
                        continue
                    if Map[nx][ny]!=0:
                        Map[nx][ny]=land
                        visit[nx][ny]=True
                        q.append([nx,ny])
            land+=1

land=1
visit=[[False]*N for _ in range(N)]
#dist=[[10001]*N for _ in range(N)]
ans=10001
for i in range(N):
    for j in range(N):
        if Map[i][j]==land and not visit[i][j]:
            
            dist_check=[[10001]*N for _ in range(N)]
            q=deque([[i,j,0]])
            visit[i][j]=True
            
            while q:
                x,y,d=q.popleft()
                
                if d>=ans:
                    continue
                
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if nx<0 or nx>=N or ny<0 or ny>=N:
                        continue
                    if dist_check[nx][ny]<=d+1 or visit[nx][ny]:
                        continue
                    
                    if Map[nx][ny]!=0:
                        if Map[nx][ny]==land:
                            visit[nx][ny]=True
                            q.append([nx,ny,0])
                            
                        # 다른 땅
                        else:
                            if ans>d+1:
                                ans=d+1
                            #if dist[nx][ny]>d+1:
                                #dist[nx][ny]=d+1
                    else:
                        dist_check[nx][ny]=d+1
                        q.append([nx,ny,d+1])
            land+=1
            
print(ans-1)