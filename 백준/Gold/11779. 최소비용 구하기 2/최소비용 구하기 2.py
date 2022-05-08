import heapq
import sys
from collections import defaultdict
input=sys.stdin.readline

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v,w=map(int,input().split())
    graph[u].append([v,w])


s,f=map(int,input().split())

min_Q=[]
dist=[float('inf')]*(n+1)
parent=defaultdict(int)
parent[s]=-1

def dijkstra(s):
    dist[s]=0
    heapq.heappush(min_Q,[0,s])
    while min_Q:
        d,u=heapq.heappop(min_Q)
        if d>dist[u]:
            continue
        for v,w in graph[u]:
            temp_w=w+d
            if temp_w<dist[v]:
                dist[v]=temp_w
                parent[v]=u
                heapq.heappush(min_Q,[temp_w,v])

dijkstra(s)
print(dist[f])
result=[]
while parent[f]!=-1:
    result.append(f)
    f=parent[f]
result.append(s)

print(len(result))
print(' '.join(map(str,result[::-1])))