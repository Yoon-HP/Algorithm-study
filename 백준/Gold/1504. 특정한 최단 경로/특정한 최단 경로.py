import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,w=map(int,input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])
    
v1,v2=map(int,input().split())

def dijkstra(graph,node):
    min_Q=[[0,node]]
    stpath=[float('inf')]*(N+1)
    stpath[node]=0
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
    return stpath

st_1=dijkstra(graph,1)
st_v1=dijkstra(graph,v1)
st_v2=dijkstra(graph,v2)

result=float('inf')
result=min(result,st_1[v1]+st_v1[v2]+st_v2[N],st_1[v2]+st_v2[v1]+st_v1[N])
if result==float('inf'):
    print(-1)
else:
    print(result)
