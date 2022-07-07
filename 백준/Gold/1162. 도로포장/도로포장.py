import sys
input=sys.stdin.readline
import heapq
def ans():
    N,M,K=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for _ in range(M):
        u,v,t=map(int,input().split())
        graph[u].append([v,t])
        graph[v].append([u,t])
        
    time=[[float('inf')]*(K+1) for _ in range(N+1)]
    time[1][0]=0
    
    h=[[0,1,0]]
    while h:
        t,u,cnt=heapq.heappop(h)
        if time[u][cnt]<t:
            continue
        for v,w in graph[u]:
            temp_t=t+w
            if time[v][cnt]>temp_t:
                time[v][cnt]=temp_t
                heapq.heappush(h,[temp_t,v,cnt])
            if cnt<K and time[v][cnt+1]>t:
                time[v][cnt+1]=t
                heapq.heappush(h,[t,v,cnt+1])
    
    print(min(time[N]))
ans()