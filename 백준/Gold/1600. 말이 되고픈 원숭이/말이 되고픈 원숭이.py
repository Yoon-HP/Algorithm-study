# 1600번 말이 되고픈 원숭이
from collections import deque
import sys
input=sys.stdin.readline

K=int(input())
W,H=map(int,input().split())

directions=[(1,0),(-1,0),(0,1),(0,-1),(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]
dk=[0,0,0,0,1,1,1,1,1,1,1,1]

Map=[]
visit=[[[float('inf') for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

for _ in range(H):
    row=list(map(int,input().split()))
    Map.append(row)

# u,v,d,k
queue=deque([[0,0,0,0]])
visit[0][0][0]=0

while queue:
    x,y,d,k=queue.popleft()
    
    index=0
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        nk=k+dk[index]
        index+=1
        
        if nx<0 or nx>=H or ny<0 or ny>=W or nk>K:
            continue
        
        if Map[nx][ny]==1:
            continue
        if visit[nx][ny][nk] > d+1:
            visit[nx][ny][nk]=d+1
            queue.append([nx,ny,d+1,nk])
        
if min(visit[H-1][W-1])==float('inf'):
    print(-1)
else:
    print(min(visit[H-1][W-1]))