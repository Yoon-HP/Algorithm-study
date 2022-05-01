import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
d=[i for i in range(n+1)]
def find(u):
    if u==d[u]:
        return u
    temp=find(d[u])
    d[u]=temp
    return d[u]

def union(u,v):
    u=find(u) ; v=find(v)
    if (u!=v):
        d[u]=v

for i in range(m):
    x,u,v=map(int,input().split())
    if x==0:
        union(u,v)
    else:
        if find(u)==find(v):
            print("YES")
        else:
            print("NO") 