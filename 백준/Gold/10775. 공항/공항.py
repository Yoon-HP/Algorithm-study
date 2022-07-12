import sys
input=sys.stdin.readline

'''
각 비행기는 g가 주어졌을 때 g번째 포트에 도킹하는걸 우선으로 해야함.
g번째 포트가 이미 차 있는 경우 g보다 작으면서 자리가 있는 포트를 찾음
시간복잡도를 줄이기 위해 분리집합을 사용해 어디부터 탐색해야 하는지 정한다.
'''

def find(u):
    if d[u]!=u:
        d[u]=find(d[u])
    return d[u]

def union(u,v):
    root_u=find(u)
    root_v=find(v)
    # root_u,root_v중 작은 것이 root가 됨
    d[max(root_u,root_v)]=min(root_u,root_v)

G=int(input())
P=int(input())

d=[i for i in range(G+1)]

check=[False]*(G+1)

cnt=0
flag=1
for _ in range(P):
    g=int(input())
    if flag:
        if not check[find(g)]:
            if find(g)<=0:
                flag=0
                continue
            cnt+=1
            check[find(g)]=True
            union(find(g),find(g)-1)
print(cnt)