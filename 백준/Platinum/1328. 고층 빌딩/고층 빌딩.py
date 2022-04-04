# 1328번 고층 빌딩
N,L,R=map(int,input().split())

dp=[[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

dp[1][1][1]=1

def building(N,L,R):
    if N<=0 or L<=0 or R<=0:
        return 0 
    if dp[N][L][R]==-1:
        return 0 
    if dp[N][L][R]!=0:
        return dp[N][L][R]
    if L>N or R>N:
        dp[N][L][R]=-1
        return 0
    if L==0 or R==0:
        dp[N][L][R]=-1
        return 0
    if N>=2:
        dp[N][L][R]=building(N-1,L-1,R)+building(N-1,L,R-1)+(N-2)*building(N-1,L,R)
        if dp[N][L][R]<=0:
            dp[N][L][R]=-1
            return 0
        return dp[N][L][R]
    else:
        if L==1 and R==1:
            return 1
        else:
            return 0
print(building(N,L,R)%1000000007) 
