from collections import deque
import sys
input=sys.stdin.readline
n,l,r=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
Map=[list(map(int,input().split())) for _ in range(n)]
cnt=1
day=0
while cnt!=0:
    cnt=0
    check=[[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                temp_index=[]
                temp_value=0
                q=deque([[i,j]])
                while q:
                    a,b=q.popleft()
                    check[a][b]=True
                    temp_index.append([a,b])
                    temp_value+=Map[a][b]
                    for k in range(4):
                        u,v=a+dx[k],b+dy[k]
                        if 0<=u<n and 0<=v<n and not check[u][v]:
                            if l<=abs(Map[a][b]-Map[u][v])<=r:
                                q.append([u,v])
                                # 여기서도 True해줘야 중복으로 카운트 하는 경우가 안생김
                                check[u][v]=True
                                cnt+=1
                for k,t in temp_index:
                    Map[k][t]=int(temp_value/len(temp_index))
    if cnt:
        day+=1
print(day)