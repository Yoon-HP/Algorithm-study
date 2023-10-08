import sys
input=sys.stdin.readline

def find(u):
    if d[u]!=u:
        d[u]=find(d[u])
    return d[u]

def union(u,v):
    root_u=find(u)
    root_v=find(v)
    if root_u != root_v:
        d[root_v]=root_u
        rank[root_u]+=rank[root_v]
    
def update(new_node):
    global cnt
    transfer[new_node]=cnt
    d.append(cnt)
    rank.append(1)
    check.add(new_node)
    cnt+=1
    
T=int(input())
for _ in range(T):
    F=int(input())
    # 새로운 사람이 들어오는지 체크하는 set
    check=set()
    
    # 새로운 사람의 수
    cnt=0
    
    # 새로운 사람이 들어왔을 때 이를 다루기 쉽게 변형
    transfer={}
    
    # 각 집합의 root를 나타냄
    d=[]
    
    # 각 집합에 속하는 사람의 수 저장 (각 집합의 root에 저장)
    rank=[]
    for _ in range(F):
        u,v=map(str,input().split())
        if u not in check:
            update(u)
        if v not in check:
            update(v)
        union(transfer[u],transfer[v])
        print(rank[find(transfer[u])])