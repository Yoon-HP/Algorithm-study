import heapq
import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])

k_time=[[float('inf')]*k for _ in range(n+1)]
heap=[[0,1]]
k_time[1][0]=0
while heap:
    t,u=heapq.heappop(heap)
    for v,w in graph[u]:
        temp_time=t+w
        if k_time[v][k-1]>temp_time:
            k_time[v][k-1]=temp_time
            k_time[v].sort()
            heapq.heappush(heap,[temp_time,v])
            
for i in range(1,n+1):
    if k_time[i][k-1]!=float('inf'):
        print(k_time[i][k-1])
    else:
        print(-1)