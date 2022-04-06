N=int(input())
pos=[0]*N #각 열에서 퀸의 위치
# 각 행에 퀸을 배치했는지 체크
flag_a=[False]*N
flag_b=[False]*(2*N-1)
flag_c=[False]*(2*N-1)

count=0
def Set(i):
    global count
    for j in range(N):
        if not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+N-1]:
            pos[i]=j
            if i==N-1:
                count+=1
            else:
                flag_a[j]=flag_b[i+j]=flag_c[i-j+N-1]=True
                Set(i+1)
                flag_a[j]=flag_b[i+j]=flag_c[i-j+N-1]=False

Set(0)
print(count)
