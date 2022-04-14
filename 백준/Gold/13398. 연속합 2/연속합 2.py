N=int(input())
S=list(map(int,input().split()))

dp=[[0,0] for i in range(N)]
dp[0]=[S[0],-1001]

for i in range(1,N):
    dp[i][0]=max(dp[i-1][0]+S[i],S[i])
    dp[i][1]=max(dp[i-1][0],dp[i-1][1]+S[i])
    
max_n=-1001
for i in dp:
    max_n=max(max_n,max(i))
print(max_n)