import sys
input=sys.stdin.readline

N,K=map(int,input().split())
table=[[0,0]]+[list(map(int,input().split())) for _ in range(N)]

dp=[[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        w=table[i][0]
        v=table[i][1]
        
        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[N][K])