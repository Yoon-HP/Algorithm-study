N = int(input())

A = list(map(int, input().split()))

dp = [1] * N
S=[[i] for i in A]
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            if dp[j]+1>dp[i]:
                dp[i]=dp[j]+1
                S[i]=S[j]+[A[i]]
print(max(dp))
key=dp.index(max(dp))
print(*S[key])