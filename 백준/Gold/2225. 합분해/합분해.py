N,K=map(int,input().split())
dp=[[0]+[1]+[0]*(K-1) for i in range(N+1)]
for i in range(2,K+1):
    for j in range(1,N+1):
        num=j
        while num!=0:
            dp[j][i]+=dp[num][i-1]%1000000000
            num-=1
        dp[j][i]+=1
print(dp[N][K]%1000000000)
