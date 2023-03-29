# 16236번 아기 상어
from collections import deque

def path_check(a,b):
    global Map, N, dx, dy, cur_i, cur_j, size
    visit=[[False]*N for _ in range(N)]
    q=deque([[cur_i,cur_j,0]])
    visit[cur_i][cur_j]=True
    while q:
        x,y,cnt=q.popleft()
        if x==a and y==b:
            return cnt
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if Map[nx][ny]>size or visit[nx][ny]:
                continue
            q.append([nx,ny,cnt+1])
            visit[nx][ny]=True
    return 0

N=int(input())
fish=[]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

Map=[list(map(int,input().split())) for _ in range(N)]

# 크기가 1~6으로 고정되어 있으므로
fish={i+1:[] for i in range(6)}

for i in range(N):
    for j in range(N):
        if Map[i][j]!=0 and Map[i][j]!=9:
            fish[Map[i][j]].append([i,j])
        if Map[i][j]==9:
            cur_i=i
            cur_j=j
            Map[i][j]=0
# 초기 상태
size=2
cnt=0

ans=0

while True:
    temp=[]
    for i in range(1,min(size,7)):
        if fish[i]:
            for j in fish[i]:
                ck_cnt=path_check(j[0],j[1])
                if ck_cnt:
                    temp.append([ck_cnt,j[0],j[1],i])
    if temp:
        temp.sort()
        Map[temp[0][1]][temp[0][2]]=0
        cur_i=temp[0][1]
        cur_j=temp[0][2]
        ans+=temp[0][0]
        cnt+=1
        fish[temp[0][3]].remove([temp[0][1],temp[0][2]])
        if size==cnt:
            size+=1
            cnt=0
    else:
        break
print(ans)