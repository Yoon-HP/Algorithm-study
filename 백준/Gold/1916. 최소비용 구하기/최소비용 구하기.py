import heapq
import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
graph=[[] for i in range(M+1)]


for i in range(M):
    u,v,w=map(int,input().split())
    graph[u].append([v,w])
start,end=map(int,input().split())

min_Q=[]
stpath=[float('inf')]*(N+1)
def dijkstra(start,end):
    stpath[start]=0
    heapq.heappush(min_Q,[0,start])
    while min_Q:
        d,u=heapq.heappop(min_Q)
        if u==end:
            break
        for v,w in graph[u]:
            temp_w=w+d
            if temp_w<stpath[v]:
                stpath[v]=temp_w
                heapq.heappush(min_Q,[temp_w,v])


dijkstra(start,end)

print(stpath[end])