import sys
import heapq
input=sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]
N=int(input())
Map=[list(input()) for _ in range(N)]
visit=[[False]*N for _ in range(N)]
heap=[]
heapq.heappush(heap,[0,0,0])
visit[0][0]=True
while heap:
    cnt,u,v=heapq.heappop(heap)
    if u==N-1 and v==N-1:
        print(cnt)
        break
    for i in range(4):
        a=u+dx[i]
        b=v+dy[i]
        if 0<=a<N and 0<=b<N and not visit[a][b]:
            if Map[a][b]=='0':
                heapq.heappush(heap,[cnt+1,a,b])
            else:
                heapq.heappush(heap,[cnt,a,b])
            visit[a][b]=True