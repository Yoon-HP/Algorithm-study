First=["0"]+list(input().rstrip())
Second=["0"]+list(input().rstrip())

remember=[set() for _ in range(len(Second))]

dp=[[0]*(len(First)) for _ in range(len(Second))]

for i in range(1,len(Second)):
    for j in range(1,len(First)):
        key=Second[i]
        if key==First[j]:
            dp[i][j]=max(dp[i-1][j-1]+1,dp[i][j-1])
            remember[i].add(dp[i][j])
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
                
key=dp[-1][-1]
result=[]
for i in range(len(Second)-1,-1,-1):
    if key in remember[i]:
        result.append(Second[i])
        key-=1
        
print(dp[-1][-1])
if result:
    print(''.join(result[::-1]))