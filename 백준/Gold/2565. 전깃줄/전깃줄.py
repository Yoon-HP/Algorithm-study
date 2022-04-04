from collections import defaultdict
import sys
input=sys.stdin.readline

N=int(input())

# A를 기준으로 B를 생각 > 교차되지 않는다. a2>a1 and b2>b1 ...
# dp[i]: 교차되지 않고 연결되는 전선의 수가 i개가 되도록 하는 전봇대 B의 최소값 

dp=[0]

A_B=defaultdict(int)
for _ in range(N):
    a,b=map(int,input().split())
    A_B[a]=b

for i in range(501):
    if A_B[i]!=0:
        if len(dp)==1:
            dp.append(A_B[i])
        else:
            if A_B[i]>dp[-1]:
                dp.append(A_B[i])
            else:
                for j in range(1,len(dp)):
                    if dp[j-1]<A_B[i]<dp[j]:
                        dp[j]=A_B[i]

print(N-len(dp)+1)