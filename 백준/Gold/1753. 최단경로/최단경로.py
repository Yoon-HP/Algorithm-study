# 다익스트라 복습 

# 1753번 최단경로

import heapq
import sys
input=sys.stdin.readline

V,E=map(int,input().split())
K=int(input())

graph=[[] for _ in range(V+1)]
dist=[float('inf') for _ in range(V+1)]

for _ in range(E):
    u,v,w=map(int,input().split())
    
    # 방향 그래프!
    graph[u].append([v,w])

# init
dist[K]=0

# 우선순위 큐 안에 가중치 값이 앞에 위치 해야함
min_Q=[[0,K]]

while min_Q:
    d,u=heapq.heappop(min_Q)
    
    if d > dist[u]:
        continue
    
    for adj,w in graph[u]:
        if d+w < dist[adj]:
            dist[adj]=d+w
            heapq.heappush(min_Q,[d+w,adj])
            
for i in range(1,V+1):
    if dist[i]==float('inf'):
        print("INF")
    else:
        print(dist[i])