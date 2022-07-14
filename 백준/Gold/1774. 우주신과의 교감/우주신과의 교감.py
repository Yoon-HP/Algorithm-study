import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())

def find(u):
    if d[u]!=u:
        d[u]=find(d[u])
    return d[u]

def union(u,v):
    root_u=find(u)
    root_v=find(v)
    d[root_v]=root_u

def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)

d=[i for i in range(N+1)]
visit=[False]*(N+1)
cnt=0
ans=0
position=[[]]+[list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    u,v=map(int,input().split())
    if find(u)!=find(v):
        if not visit[u]:
            visit[u]=True
            cnt+=1
        if not visit[v]:
            visit[v]=True
            cnt+=1
        union(u,v)
h=[]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i!=j:
            heapq.heappush(h,[dist(position[i],position[j]),i,j])
while h:
    if cnt==N:
        break
    w,a,b=heapq.heappop(h)
    if find(a)!=find(b):
        if not visit[u]:
            visit[u]=True
            cnt+=1
        if not visit[v]:
            cnt+=1
            visit[v]=True
        union(a,b)
        ans+=w
print(f'{ans:.2f}')