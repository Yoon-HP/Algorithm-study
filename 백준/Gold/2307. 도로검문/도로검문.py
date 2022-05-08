import heapq
from collections import defaultdict
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v,w=map(int,input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

min_Q=[]
dist=[float('inf')]*(n+1)
parent=defaultdict(int)
parent[1]=-1

def dijkstra(s):
    dist[s]=0
    heapq.heappush(min_Q,[0,s])
    while min_Q:
        d,u=heapq.heappop(min_Q)
        # 불필요한 과정은 패스하자.
        if d>dist[u]:
            continue
        for v,w in graph[u]:
            temp_w=w+d
            if temp_w<dist[v]:
                dist[v]=temp_w
                parent[v]=u
                heapq.heappush(min_Q,[temp_w,v])
s=1;f=n
dijkstra(s)
Min=dist[f]
path=[]
while parent[f]!=-1:
    path.append(f)
    f=parent[f]
path.append(s)
path.reverse()

result=[]
flag=True
for i in range(len(path)-1):
    dist=[float('inf')]*(n+1)
    min_Q=[]
    u,v=path[i],path[i+1]
    w=0
    for j in graph[u]:
        if j[0]==v:
            w=j[1]
    graph[u].remove([v,w])
    graph[v].remove([u,w])
    dijkstra(s)
    if dist[n]==float('inf'):
        print(-1)
        flag=False
        break
    else:
        result.append(dist[n]-Min)
    graph[u].append([v,w])
    graph[v].append([u,w])
    
if flag:
    print(max(result))