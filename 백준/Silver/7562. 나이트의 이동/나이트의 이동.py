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
    if u==fu and v==fv:
        print(0)
    else:
        visited=[[0]*I for _ in range(I)]
        q=deque([[u,v]])
        while q:
            y,x=q.popleft()
            for i in range(8):
                a,b=y+dy[i],x+dx[i]
                if 0<=a<I and 0<=b<I:
                    if visited[a][b]==0:
                        if a==fu and b==fv:
                            q=deque([])
                            print(visited[y][x]+1)
                            break
                        q.append([a,b])
                        visited[a][b]=visited[y][x]+1