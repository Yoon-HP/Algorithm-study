First=["0"]+list(input().rstrip())
Second=["0"]+list(input().rstrip())

dp=[[0]*(len(First)) for _ in range(len(Second))]

for i in range(1,len(Second)):
    for j in range(1,len(First)):
        key=Second[i]
        if key==First[j]:
            dp[i][j]=max(dp[i-1][j-1]+1,dp[i][j-1])
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])