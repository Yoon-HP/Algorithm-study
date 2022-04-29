import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n=int(input())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    u,v,w=map(int,input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

def tree_dia(x,l):
    for i in graph[x]:
        a,b=i
        if distance[a]==-1:
            distance[a]=l+b
            tree_dia(a,l+b)
            
distance=[-1]*(n+1)
distance[1]=0
tree_dia(1,0)

start=distance.index(max(distance))
distance=[-1]*(n+1)
distance[start]=0
tree_dia(start,0)
print(max(distance))