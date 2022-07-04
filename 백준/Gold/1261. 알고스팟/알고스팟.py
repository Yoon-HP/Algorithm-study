from collections import deque
import sys
input=sys.stdin.readline

M,N=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
Map=[list(input()) for _ in range(N)]
check=[[False]*M for _ in range(N)]
q=deque([[0,0,0]])
check[0][0]=True
while q:
    u,v,cnt=q.popleft()
    if (u==N-1 and v==M-1):
        print(cnt)
        break
    for i in range(4):
        a=u+dx[i]
        b=v+dy[i]
        if 0<=a<N and 0<=b<M and not check[a][b]:
            if Map[a][b]=='0':
                q.appendleft([a,b,cnt])
            else:
                q.append([a,b,cnt+1])
            check[a][b]=True
            