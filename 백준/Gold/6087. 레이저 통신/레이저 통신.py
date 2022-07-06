import heapq
import sys
input=sys.stdin.readline
W,H=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]

razer=[]
Map=[list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if Map[i][j]=='C':
            razer.append([i,j])

heap=[[-1]+razer[0]+[-1]]

visit=[[float('inf')]*(W) for _ in range(H)]
visit[razer[0][0]][razer[0][1]]=-1
while heap:
    cnt,u,v,dir=heapq.heappop(heap)
    for i in range(4):
        a=u+dx[i]
        b=v+dy[i]
        if 0<=a<H and 0<=b<W:
            if Map[a][b]=='.' or Map[a][b]=='C':
                if i!=dir:
                    if cnt+1<=visit[a][b]:
                        heapq.heappush(heap,[cnt+1,a,b,i])
                        visit[a][b]=cnt+1
                else:
                    if cnt<=visit[a][b]:
                        heapq.heappush(heap,[cnt,a,b,i])
                        visit[a][b]=cnt

print(visit[razer[1][0]][razer[1][1]])