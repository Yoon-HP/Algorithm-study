import heapq #prims 알고리즘은 한 단계 진행할때마다 무조건 하나는 확정됨
import sys
input=sys.stdin.readline

V,E=map(int,input().split())
visited=[False]*(V+1)
graph=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())

    graph[u].append([w,v])
    graph[v].append([w,u])
    
q=[[0,1]]
answer=0
cnt=0
while q:
    if cnt==V:
        break
    w,s=heapq.heappop(q)
    if not visited[s]:
        visited[s]=True
        answer+=w
        cnt+=1
        for i in graph[s]:
            heapq.heappush(q,i)          
print(answer)