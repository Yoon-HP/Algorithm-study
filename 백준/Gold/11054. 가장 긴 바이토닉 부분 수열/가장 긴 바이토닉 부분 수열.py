N=int(input())
A=list(map(int,input().split()))

dp_L=[1]*N
dp_R=[1]*N
dp=[0]*N

for i in range(N):
    for j in range(i):
        if A[i]>A[j]:
            dp_L[i]=max(dp_L[i],dp_L[j]+1)
    dp[i]+=dp_L[i]
            
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if A[i]>A[j]:
            dp_R[i]=max(dp_R[i],dp_R[j]+1)
    dp[i]+=dp_R[i]
        

print(max(dp)-1)