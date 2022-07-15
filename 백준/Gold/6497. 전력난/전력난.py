import heapq
import sys
input=sys.stdin.readline

def find(u):
    if d[u]!=u:
        d[u]=find(d[u])
    return d[u]

def union(u,v):
    root_u=find(u)
    root_v=find(v)
    d[root_v]=root_u

while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    d=[i for i in range(m)]
    cnt=0
    ans=0
    h=[]
    max_price=0
    for _ in range(n):
        x,y,z=map(int,input().split())
        max_price+=z
        heapq.heappush(h,[z,x,y])
    while h:
        if cnt==m-1:
            break
        w,u,v=heapq.heappop(h)
        if find(u)!=find(v):
            union(u,v)
            cnt+=1
            ans+=w
    print(max_price-ans)