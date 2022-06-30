import heapq
import sys
input=sys.stdin.readline

N,M,X=map(int,input().split())
front=[[] for _ in range(N+1)]
back=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,w=map(int,input().split())
    # 노드 X에서 각 노드로 가는 최단경로를 구하는데 사용
    front[u].append([v,w])
    # 각 노드에서 노드 X까지 가는 최단경로를 구하는데 사용
    back[v].append([u,w])

def dijkstra(graph):
    min_Q=[[0,X]]
    stpath=[float('inf')]*(N+1)
    stpath[X]=0
    while min_Q:
        d,u=heapq.heappop(min_Q)
        # 이미 최단경로가 확정된 노드에 대해 불필요한 연산을 줄임
        if stpath[u]<d:
            continue
        for v,w in graph[u]:
            temp_w=w+d
            if temp_w<stpath[v]:
                stpath[v]=temp_w
                heapq.heappush(min_Q,[temp_w,v])
    for i in range(1,len(stpath)):
        result[i]+=stpath[i]
                
result=[0]*(N+1)
dijkstra(front)
dijkstra(back)
print(max(result))