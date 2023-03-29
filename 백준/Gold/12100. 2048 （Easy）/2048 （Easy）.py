# 12100번 2048 (Easy)
import copy
N=int(input())
Map=[list(map(int,input().split())) for _ in range(N)]

# flag 추가
for i in range(N):
    for j in range(N):
        Map[i][j]=[Map[i][j],0]

dr=[1,-1,0,0]
dc=[0,0,1,-1]


def decimal_to_quaternary(n:int,k):
    result=''
    while n:
        result+=f'{n%4}'
        n=int(n/4)
    return result[::-1].zfill(k)

def manager(s):
    for i in s:
        if i=='0':
            up()
        elif i=='1':
            right()
        elif i=='2':
            down()
        else:
            left()

def ans_check():
    global Map,N
    ans=0
    for i in range(N):
        for j in range(N):
            ans=max(ans,Map[i][j][0])
    return ans

def up():
    global Map,N
    for j in range(N):
        for i in range(N):
            if Map[i][j][0]!=0:
                di=i
                while True:
                    di=di+dr[1]
                    if di<0:
                        break
                    if Map[di][j][0]==0:
                        # 빈칸이 있어서 위로 올림
                        Map[di][j][0]=Map[di-dr[1]][j][0]
                        Map[di][j][1]=0
                        Map[di-dr[1]][j]=[0,0]
                        continue
                    
                    if Map[di][j][1]==1:
                        break
                    if Map[di][j][0]==Map[di-dr[1]][j][0]:
                        Map[di][j][0]*=2
                        Map[di][j][1]=1
                        Map[di-dr[1]][j]=[0,0]
                        break
                    else:
                        break
        for i in range(N):
            Map[i][j][1]=0        
def down():
    global Map,N
    for j in range(N):
        for i in range(N):
            if Map[N-i-1][j][0]!=0:
                di=N-i-1
                while True:
                    di=di+dr[0]
                    if di>=N:
                        break
                    if Map[di][j][0]==0:
                        # 빈칸이 있어서 위로 올림
                        Map[di][j][0]=Map[di-dr[0]][j][0]
                        Map[di][j][1]=0
                        Map[di-dr[0]][j]=[0,0]
                        continue
                    
                    if Map[di][j][1]==1:
                        break
                    if Map[di][j][0]==Map[di-dr[0]][j][0]:
                        Map[di][j][0]*=2
                        Map[di][j][1]=1
                        Map[di-dr[0]][j]=[0,0]
                        break
                    else:
                        break
        for i in range(N):
            Map[i][j][1]=0

def left():
    global Map,N
    for i in range(N):
        for j in range(N):
            if Map[i][j][0]!=0:
                dj=j
                while True:
                    dj=dj+dc[3]
                    if dj<0:
                        break
                    if Map[i][dj][0]==0:
                        Map[i][dj][0]=Map[i][dj-dc[3]][0]
                        Map[i][dj][1]=0
                        Map[i][dj-dc[3]]=[0,0]
                        continue
                    
                    if Map[i][dj][1]==1:
                        break
                    if Map[i][dj][0]==Map[i][dj-dc[3]][0]:
                        Map[i][dj][0]*=2
                        Map[i][dj][1]=1
                        Map[i][dj-dc[3]]=[0,0]
                        break
                    else:
                        break
        for j in range(N):
            Map[i][j][1]=0

def right():
    global Map,N
    for i in range(N):
        for j in range(N):
            if Map[i][N-j-1][0]!=0:
                dj=N-j-1
                while True:
                    dj=dj+dc[2]
                    if dj>=N:
                        break
                    if Map[i][dj][0]==0:
                        Map[i][dj][0]=Map[i][dj-dc[2]][0]
                        Map[i][dj][1]=0
                        Map[i][dj-dc[2]]=[0,0]
                        continue
                    
                    if Map[i][dj][1]==1:
                        break
                    if Map[i][dj][0]==Map[i][dj-dc[2]][0]:
                        Map[i][dj][0]*=2
                        Map[i][dj][1]=1
                        Map[i][dj-dc[2]]=[0,0]
                        break
                    else:
                        break
        for j in range(N):
            Map[i][j][1]=0

temp_Map=copy.deepcopy(Map)
ans=2
for i in range(4**5):
    manager(decimal_to_quaternary(i,5))
    ans=max(ans,ans_check())
    Map=copy.deepcopy(temp_Map)
    
print(ans)
    
