N=int(input())
dp=[float('inf')]*(N+1)
if N==1:
    print(0)
    print(1)
elif N==2 or N==3:
    print(1)
    print(N,1)
else:
    dp[1],dp[2],dp[3]=0,1,1
    for i in range(4,N+1):
        if i%2==0 and i%3==0:
            dp[i]=min(dp[i],dp[i-1]+1,dp[i//2]+1,dp[i//3]+1)
        elif i%2==0:
            dp[i]=min(dp[i],dp[i-1]+1,dp[i//2]+1)
        elif i%3==0:
            dp[i]=min(dp[i],dp[i-1]+1,dp[i//3]+1)
        else:
            dp[i]=min(dp[i],dp[i-1]+1)
    
    print(dp[N])
    current=dp[N]
    index=N
    result=[N]
    while current!=0:
        if dp[index-1]==current-1:
            current=dp[index-1]
            index-=1
            result.append(index)
            continue
        if index%2==0:
            if dp[int(index/2)]==current-1:
                current=dp[int(index/2)]
                index=int(index/2)
                result.append(index)
                continue
        if index%3==0:
            if dp[int(index/3)]==current-1:
                current=dp[int(index/3)]
                index=int(index/3)
                result.append(index)
    print(*result)