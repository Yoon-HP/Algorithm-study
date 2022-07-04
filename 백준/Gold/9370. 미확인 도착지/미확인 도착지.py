import heapq
import sys
input=sys.stdin.readline

def dijkstra(graph,node,n):
    min_Q=[[0,node]]
    stpath=[float('inf')]*(n+1)
    stpath[node]=0
    while min_Q:
        d,u=heapq.heappop(min_Q)
        if stpath[u]<d:
            continue
        for v,w in graph[u]:
            temp_w=w+d
            if temp_w<stpath[v]:
                stpath[v]=temp_w
                heapq.heappush(min_Q,[temp_w,v])
    return stpath

T=int(input())
for _ in range(T):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d=map(int,input().split())
        if (a==g and b==h) or (a==h and b==g):
            d-=0.1
        graph[a].append([b,d])
        graph[b].append([a,d])
        
    candidate_node=[]
    for _ in range(t):
        candidate_node.append(int(input()))
    candidate_node.sort()
    path=dijkstra(graph,s,n)
    for i in candidate_node:
        if type(path[i])==float and path[i]!=float('inf'):
            print(i,end=' ')
    print()