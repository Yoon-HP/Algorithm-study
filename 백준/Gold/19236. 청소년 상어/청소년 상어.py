# 19236번 청소년 상어
import copy

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

# 초기 정보 세팅
fish={}
Map=[[[] for _ in range(4)] for _ in range(4)]
for i in range(4):
    row=list(map(int,input().split()))
    for j in range(8):
        if j%2==0:
            fish[row[j]]=[i,int(j/2)]
            Map[i][int(j/2)].append(row[j])
        else:
            Map[i][int(j/2)].append(row[j]-1)

ans=Map[0][0][0]
# 상어가 처음 수조에 들어온 상황!
cur_i,cur_j=fish[Map[0][0][0]]

del fish[Map[0][0][0]]

dir=Map[0][0][1]
Map[0][0][0]=-1
Map[0][0][1]=dir


# 상어가 한번 움직이고 난 후 호출되는 함수!
def fish_move():
    global Map, fish, dx, dy
    for i in range(1,17):
        # 아직 물고기가 수조 안에 있다면.
        if i in fish:
            
            temp_dir=Map[fish[i][0]][fish[i][1]][1]
            temp_x,temp_y=fish[i]
            
            for j in range(8):
                nx=temp_x+dx[(temp_dir+j)%8]
                ny=temp_y+dy[(temp_dir+j)%8]
                
                if nx<0 or nx>=4 or ny<0 or ny>=4:
                    continue
                # 상어가 있는 경우
                if Map[nx][ny][0]==-1:
                    continue
                
                # 빈칸인 경우
                if Map[nx][ny][0]==0:
                    # 물고기 위치 변경
                    fish[i]=[nx,ny]
                    
                    Map[nx][ny][0]=i
                    Map[nx][ny][1]=(temp_dir+j)%8
                    
                    Map[temp_x][temp_y]=[0,0]
                    break
                # 여기까지 왔다면... 이동하고자 하는 위치에 다른 물고기가 존재하는 경우 서로 자리 변경
                fish[i],fish[Map[nx][ny][0]]=fish[Map[nx][ny][0]], fish[i]
                Map[nx][ny],Map[temp_x][temp_y]=Map[temp_x][temp_y],Map[nx][ny]
                Map[nx][ny][1]=(temp_dir+j)%8
                break


def move(cur_i,cur_j,dir,cur_ans):
    global Map, fish, dx, dy, ans
    x=cur_i
    y=cur_j
    cnt=0
    
    # undo 역할
    temp_Map=copy.deepcopy(Map)
    temp_fish=copy.deepcopy(fish)
    
    fish_move()

    nx=x
    ny=y
    while True:
        nx=nx+dx[dir]
        ny=ny+dy[dir]
        if nx<0 or nx>=4 or ny<0 or ny>=4:
            break
            
        # 현재 칸에 물고기가 위치해 있는 경우
        if Map[nx][ny][0]!=0:
            cnt+=1
            
            # 상어가 원래 있던 곳은 빈칸으로 변경
            Map[x][y]=[0,0]
            
            number=Map[nx][ny][0]
            cur_i,cur_j=fish[number]
            ndir=Map[nx][ny][1]
            del fish[number]
            Map[nx][ny]=[-1,ndir]
            
            move(cur_i,cur_j,ndir,cur_ans+number)
            
            # undo 작업 진행
            Map[x][y]=[-1,dir]
            fish[number]=[nx,ny]
            Map[nx][ny]=[number,ndir]

        
    if cnt==0:
        ans=max(ans,cur_ans)
    # undo 작업 진행!!
    Map=temp_Map
    fish=temp_fish
    
    
move(cur_i,cur_j,dir,ans)

print(ans)