from collections import deque
import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    dx=[2,2,1,1,-1,-1,-2,-2]
    dy=[1,-1,2,-2,2,-2,1,-1]
    I=int(input())
    u,v=map(int,input().split())
    fu,fv=map(int,input().split())
    visited=[[0]*I for _ in range(I)]
    q=deque([[u,v]])
    while q:
        y,x=q.popleft()
        if y==fu and x==fv:
            print(visited[y][x])
            break
        for i in range(8):
            a,b=y+dy[i],x+dx[i]
            if 0<=a<I and 0<=b<I and visited[a][b]==0:
                q.append([a,b])
                visited[a][b]=visited[y][x]+1
