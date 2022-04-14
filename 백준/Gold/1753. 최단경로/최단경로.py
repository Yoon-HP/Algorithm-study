import heapq
import sys
input=sys.stdin.readline

V,E=map(int,input().split())
start=int(input())
graph=[[] for i in range(V+1)]


for i in range(E):
    u,v,w=map(int,input().split())
    graph[u].append([v,w])


min_Q=[]
stpath=[float('inf')]*(V+1)
def dijkstra(start):
    stpath[start]=0
    heapq.heappush(min_Q,[0,start])
    while min_Q:
        d,u=heapq.heappop(min_Q)
        for v,w in graph[u]:
            temp_w=w+d
            if temp_w<stpath[v]:
                stpath[v]=temp_w
                heapq.heappush(min_Q,[temp_w,v])


dijkstra(start)

for i in range(1,V+1):
    if stpath[i]==float('inf'):
        print("INF")
    else:
        print(stpath[i])