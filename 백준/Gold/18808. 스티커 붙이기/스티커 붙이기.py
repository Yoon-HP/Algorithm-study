# 18808번 스티커 붙이기 G3
import sys
input=sys.stdin.readline

def rotate_list(r,c,temp_list):
    # 90도 회전한 다음의 모습 만들어두기
    result=[['0']*r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            result[i][r-j-1]=temp_list[j][i]
    return result


def check(i,j,r_k,c_k):
    global temp_s,Map
    for dr in range(i,i+r_k):
        for dc in range(j,j+c_k):
            if temp_s[dr-i][dc-j]=='1':
                if Map[dr][dc]=='1':
                    return False
    return True

N,M,K=map(int,input().split())

Map=[['0']*M for _ in range(N)]

# 스티커 정보 관리
s=[]
for _ in range(K):
    r,c=map(int,input().split())
    temp=[input().split() for _ in range(r)]
    s.append([r,c,temp])

for index in range(K):
    # 아직 스티커를 붙일 장소를 찾지 못한 경우
    flag=False
    
    # 총 세번 회전 가능
    cnt=0
    while flag!=True and cnt<=3:
        if cnt==0:
            # 처음 스티커 모양의 크기
            r_k,c_k=s[index][0],s[index][1]
            temp_s=s[index][2]
            
        else:
            temp_s=rotate_list(r_k,c_k,temp_s)
            r_k,c_k=c_k,r_k
            
        temp_flag=False
        
        for i in range(N-r_k+1):
            if temp_flag:
                break
            for j in range(M-c_k+1):
                if temp_flag:
                    break
                temp_flag=check(i,j,r_k,c_k)
                
                # 스티커를 붙일 수 있다면!
                if temp_flag:
                    for dr in range(i,i+r_k):
                        for dc in range(j,j+c_k):
                            # 주의!! '0'으로 업데이트 되지 않도록
                            if temp_s[dr-i][dc-j]=='1':
                                Map[dr][dc]=temp_s[dr-i][dc-j]
        if temp_flag:
            flag=True
        else:
            cnt+=1
            
ans=0
for i in range(N):
    for j in range(M):
        if Map[i][j]=='1':
            ans+=1
print(ans)
