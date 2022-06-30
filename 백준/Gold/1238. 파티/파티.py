import heapq
import sys
input=sys.stdin.readline

N,M,X=map(int,input().split())
path=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,w=map(int,input().split())
    path[u].append([v,w])


def dijkstra(start):
    min_Q=[]
    stpath[start]=0
    heapq.heappush(min_Q,[0,start])
    while min_Q:
        d,u=heapq.heappop(min_Q)
        if start!=X and u==X:
            break
        for v,w in path[u]:
            temp_w=w+d
            if temp_w<stpath[v]:
                stpath[v]=temp_w
                heapq.heappush(min_Q,[temp_w,v])    
result=[0]*(N+1)
stpath=[float('inf')]*(N+1)
dijkstra(X)
for i in range(len(stpath)):
    result[i]+=stpath[i]
for i in range(1,N+1):
    stpath=[float('inf')]*(N+1)
    dijkstra(i)
    result[i]+=stpath[X]
result[0]=0
print(max(result))