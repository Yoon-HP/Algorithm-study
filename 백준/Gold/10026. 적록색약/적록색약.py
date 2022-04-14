from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
table=[list(input())for i in range(N)]
visited=[[False]*N for i in range(N)]
cnt=0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            q=deque([[j,i]])
            color=table[i][j]
            visited[i][j]=True
            cnt+=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    a,b=x+dx[k],y+dy[k]
                    if 0<=a<N and 0<=b<N:
                        if table[b][a]==color and not visited[b][a]:
                            visited[b][a]=True
                            q.append([a,b])
                        
visited=[[False]*N for i in range(N)]
BV=0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            q=deque([[j,i]])
            color=table[i][j]
            visited[i][j]=True
            if color=="R" or color=="G":
                color="RG"
            BV+=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    a,b=x+dx[k],y+dy[k]
                    if 0<=a<N and 0<=b<N and table[b][a] in color and not visited[b][a]:
                        visited[b][a]=True
                        q.append([a,b])
print(cnt,BV)