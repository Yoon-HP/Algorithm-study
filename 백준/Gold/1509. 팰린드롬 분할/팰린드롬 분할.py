import collections

String=list(input().rstrip())

dp_dict=collections.defaultdict(list)

table=collections.defaultdict(list)

for i in range(len(String)):
    if not table[String[i]]:
        # index 저장
        table[String[i]].append(i)
    else:
        for j in table[String[i]]:
            if i-j<=2:
                dp_dict[j].append(i)
            else:
                if i-1 in dp_dict[j+1]:
                    dp_dict[j].append(i)
        table[String[i]].append(i)

dp=[2501 for _ in range(len(String))]
dp[0]=1
for i in range(len(String)):
    if dp_dict[i]:
        for j in dp_dict[i]:
            dp[j]=min(dp[j],dp[i-1]+1,dp[j-1]+1,i+1)
            
    dp[i]=min(dp[i],dp[i-1]+1)
            
print(dp[-1])
        