# 2573번 빙산
from collections import deque
import copy

N,M=map(int,input().split())

# 얼음이 녹아서 바다가 된 시각은 문자열로 다룸 (구현상의 편의를 위해)
Map=[]
ice=[]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

# return 값 0:얼음 모두 녹음, 1: 아직 분리 안됨, -1: 분리 됨
def ans_check():
    global Map, ice, N, M, dx, dy
    cnt=0
    visit=[[False]*M for _ in range(N)]
    if ice:
        check_q=deque([ice[0]])
        visit[ice[0][1]][ice[0][2]]=True
        cnt+=1
        while check_q:
            value, x, y=check_q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if nx<0 or nx>=N or ny<0 or ny>=M:
                    continue
                
                if visit[nx][ny]:
                    continue
                
                if Map[nx][ny]!=0 and type(Map[nx][ny]) is int:
                    visit[nx][ny]=True
                    check_q.append([Map[nx][ny],nx,ny])
                    cnt+=1
        if cnt==len(ice):
            return 1
        else:
            return -1
    else:
        return 0
    

for i in range(N):
    temp_row=list(map(int,input().split()))
    Map.append(temp_row)
    for j in range(M):
        if temp_row[j]:
            ice.append([temp_row[j],i,j])
    

ice.sort()
year=0
ans=0
while True:
    
    ck=ans_check()
    if ck==0:
        ans=0
        break
    elif ck==-1:
        ans=year
        break
    
    temp=[]
    for land in ice:
        temp_cnt=0
        cur_value, cur_x, cur_y=land
        for i in range(4):
            nx=cur_x+dx[i]
            ny=cur_y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if Map[nx][ny]==0:
                temp_cnt+=1
                
            if type(Map[nx][ny]) is str:
                if int(Map[nx][ny])<year:
                    temp_cnt+=1
                    
        # 얼음이 모두 녹은 경우
        if cur_value-temp_cnt<=0:
            Map[cur_x][cur_y]=str(year)
        else:
            temp.append([cur_value-temp_cnt,cur_x,cur_y])
            
    ice=copy.deepcopy(temp)
    ice.sort()
    year+=1

print(ans)