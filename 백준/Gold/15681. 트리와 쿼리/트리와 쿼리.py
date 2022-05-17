import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
N,R,Q=map(int,input().split())
edges=[[] for _ in range(N+1)]
child=[[] for _ in range(N+1)]
parent=[-1]*(N+1)
size=[-1]*(N+1)

for _ in range(N-1):
    u,v=map(int,input().split())
    edges[u].append(v)
    edges[v].append(u)

def maketree(cN,p):
    for node in edges[cN]:
        if node!=p:
            child[cN].append(node)
            parent[node]=cN
            maketree(node,cN)

def countSubtreeNodes(cN):
    size[cN]=1
    for node in child[cN]:
        countSubtreeNodes(node)
        size[cN]+=size[node]

maketree(R,-1)
countSubtreeNodes(R)

for _ in range(Q):    
    q=int(input())
    print(size[q])