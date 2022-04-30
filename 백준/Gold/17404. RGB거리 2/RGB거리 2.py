N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
ans=float('inf')
for i in range(3):
    dp=[[float('inf'),float('inf'),float('inf')] for _ in range(N)]
    dp[0][i]=A[0][i]
    for j in range(1,N):
        dp[j][0]=min(dp[j-1][1],dp[j-1][2])+A[j][0]
        dp[j][1]=min(dp[j-1][0],dp[j-1][2])+A[j][1]
        dp[j][2]=min(dp[j-1][0],dp[j-1][1])+A[j][2]
    for j in range(3):
        if i!=j:
            ans=min(ans,dp[-1][j])
print(ans)