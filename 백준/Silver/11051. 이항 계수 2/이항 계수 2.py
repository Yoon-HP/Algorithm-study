N,K=map(int,input().split())
dp=[[1]*1001 for _ in range(1001)]
dp[2][1]=2

#파스칼 삼각형 이용
for i in range(3,1001):
    for j in range(1,i):
        dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%10007
        
print(dp[N][K])