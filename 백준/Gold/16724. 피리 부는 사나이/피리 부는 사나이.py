import sys
input=sys.stdin.readline

N,M=map(int,input().split())

dir_map=[list(input()) for _ in range(N)]

check_map=[[0 for _ in range(M)] for _ in range(N)]

def path(u,v,cnt):
    global safezone
    while True:
        if check_map[u][v]==0:
            check_map[u][v]=cnt
        else:
            if check_map[u][v]==cnt:
                safezone+=1
            break
        
        if dir_map[u][v]=='D':
            u+=1
        elif dir_map[u][v]=='U':
            u-=1
        elif dir_map[u][v]=='L':
            v-=1
        else:
            v+=1

cnt=0
safezone=0
for i in range(N):
    for j in range(M):
        if check_map[i][j]==0:
            cnt+=1
            path(i,j,cnt)
print(safezone)  