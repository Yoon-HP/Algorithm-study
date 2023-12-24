# 6593번 상범빌딩
from collections import deque
import sys
input=sys.stdin.readline

dx=[1,0,-1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,1,-1]

while True:
    L,R,C=map(int,input().strip().split())
    if L==0 and R==0 and C==0:
        break
    
    # 층,열,행
    visit=[[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    
    Map=[[] for _ in range(L)]
    
    start_point=[]
    end_point=[]
    for i in range(L):
        for j in range(R):
            row=list(input().strip())
            Map[i].append(row)
            for k in range(C):
                if row[k]=='S':
                    # 층, 열, 행
                    start_point=[i,j,k,0]
                if row[k]=='E':
                    end_point=[i,j,k,0]
        space=input()
    
    queue=deque([start_point])
    
    visit[start_point[0]][start_point[1]][start_point[2]]=True
    
    flag=True
    while queue:
        z,x,y,d=queue.popleft()
        
        if z==end_point[0] and x==end_point[1] and y==end_point[2]:
            print(f"Escaped in {d} minute(s).")
            flag=False
            break
        
        for i in range(6):
            nz,nx,ny=z+dz[i],x+dx[i],y+dy[i]
            
            if nz<0 or nz>=L or nx<0 or nx>=R or ny<0 or ny>=C:
                continue
            
            if visit[nz][nx][ny] or Map[nz][nx][ny]=='#':
                continue
            
            visit[nz][nx][ny]=True
            queue.append([nz,nx,ny,d+1])
            
    if flag:
        print("Trapped!")