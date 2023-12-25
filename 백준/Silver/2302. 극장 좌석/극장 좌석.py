# 2302번 극장 좌석


# 1<=N<=40
N=int(input())
M=int(input())



dp=[0]*(41)
dp[0]=1
dp[1]=1
dp[2]=2
for i in range(3,N+1):
    dp[i]=dp[i-1]+dp[i-2]

fix_number=[]
for _ in range(M):
    fix_number.append(int(input()))

fix_number.sort()

ans=1

pos=1

while fix_number:
    cur=fix_number.pop(0)
    ans*=dp[cur-pos]
    pos=cur+1

ans*=dp[N+1-pos]
print(ans)