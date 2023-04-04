# 4179번 불!
from collections import deque
import sys
input=sys.stdin.readline
# 아이디어 불이 확산된 모양을 먼저 계산한 후 지훈이를 이동하면 될듯
dx=[1,-1,0,0]
dy=[0,0,1,-1]
R,C=map(int,input().split())
Map=[]
me=[]
fire=[]
for row in range(R):
    temp=list(input().strip())
    for index in range(len(temp)):
        # 지훈이 초기 위치
        if temp[index]=='J':
            me.append([row,index])
        elif temp[index]=='F':
            fire.append([row,index])
    Map.append(temp)

# 불이 퍼져나가는 양상 Map에 추가
f_visit=[[-1]*C for _ in range(R)]

q=deque([])
for f in fire:
    # 초기 불 위치 큐에 추가
    q.append(f)
    f_visit[f[0]][f[1]]=0
    
while q:
    cur=q.popleft()
    for i in range(4):
        nx=cur[0]+dx[i]
        ny=cur[1]+dy[i]
        if nx<0 or nx>=R or ny<0 or ny>=C:
            continue
        # 이미 방문했거나 벽인 경우엔 지나가지 못함
        if f_visit[nx][ny]>=0 or Map[nx][ny]=='#':
            continue
        f_visit[nx][ny]=f_visit[cur[0]][cur[1]]+1
        q.append([nx,ny])

q=deque([])
visit=[[-1]*C for _ in range(R)]
for m in me:
    q.append(m)
    visit[m[0]][m[1]]=0

ans=False
a_time=0
flag=True
while q and flag:
    cur=q.popleft()
    for i in range(4):
        nx=cur[0]+dx[i]
        ny=cur[1]+dy[i]
        # 탈출에 성공한 것
        if nx<0 or nx>=R or ny<0 or ny>=C:
            ans=True
            a_time=visit[cur[0]][cur[1]]+1
            flag=False
            break
        if visit[nx][ny]>=0 or Map[nx][ny]=='#':
            continue
        if (f_visit[nx][ny]!=-1 and (f_visit[nx][ny]<=(visit[cur[0]][cur[1]]+1))):
            continue
        visit[nx][ny]=visit[cur[0]][cur[1]]+1
        q.append([nx,ny])
        
if ans:
    print(a_time)
else:
    print("IMPOSSIBLE")