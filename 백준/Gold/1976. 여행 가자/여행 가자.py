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

n=int(input())
m=int(input())
d=[i for i in range(n+1)]

for i in range(1,n+1):
    row=[-1]+list(map(int,input().split()))
    for j in range(1,len(row)):
        if row[j]==1:
            union(i,j)
            
check=list(map(int,input().split()))
start_root=find(check[0])

ans=True
for i in range(1,len(check)):
    if find(check[i])!=start_root:
        ans=False
        break
if ans:
    print("YES")
else:
    print("NO")