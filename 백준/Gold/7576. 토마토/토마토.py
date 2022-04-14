from collections import deque
import sys
input=sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
M,N=map(int,input().split())
graph=[]
count=0
tomato=deque([])
for i in range(N):
    row=list(map(int,input().split()))
    for j in range(M):
        if row[j]==1:
            tomato.append([i,j])
    graph.append(row)

def bfs():
    while tomato:
        u,v=tomato.popleft()
        for i in range(4):
            y=u+dx[i]
            x=v+dy[i]
            if 0<=y<N and 0<=x<M and graph[y][x]==0:
                graph[y][x]=graph[u][v]+1
                tomato.append([y,x])
bfs()
day=-2
empty=False
for i in graph:
    for j in i:
        if j==0:
            empty=True
        day=max(day,j)

if empty:
    print(-1)
elif day==-1:
    print(0)
else:
    print(day-1)