import heapq
import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
station=list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,w=map(int,input().split())
    graph[u].append([w,v])
    graph[v].append([w,u])

q=[]
for i in station:
    q.append([0,i])
    
answer=0
cnt=0
visited=[False]*(N+1)
while q:
    if cnt==N:
        break
    w,s=heapq.heappop(q)
    if not visited[s]:
        visited[s]=True
        answer+=w
        cnt+=1
        for i in graph[s]:
            heapq.heappush(q,i)
print(answer)