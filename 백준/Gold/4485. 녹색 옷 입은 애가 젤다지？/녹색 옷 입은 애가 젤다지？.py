import heapq
import sys
input=sys.stdin.readline

cnt=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
while True:
    N=int(input())
    if N==0:
        break
    else:
        cnt+=1
        Map=[list(map(int,input().split())) for _ in range(N)]
        visit=[[False]*N for _ in range(N)]
        heap=[]
        heapq.heappush(heap,[Map[0][0],0,0])
        visit[0][0]=True
        while heap:
            lost_m,u,v=heapq.heappop(heap)
            if u==N-1 and v==N-1:
                print(f'Problem {cnt}: {lost_m}')
            for i in range(4):
                a=u+dx[i]
                b=v+dy[i]
                if 0<=a<N and 0<=b<N and not visit[a][b]:
                    heapq.heappush(heap,[lost_m+Map[a][b],a,b])
                    visit[a][b]=True
                    