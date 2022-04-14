from collections import deque
import copy
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
house=deque([])
chicken=deque([])
d=[]
for i in range(N):
    row=list(map(int,input().split()))
    for j in range(N):
        if row[j]==1:
            house.append([i,j])
        if row[j]==2:
            chicken.append([i,j])


s=deque([])
def f():
    if len(s)==M:
        dp=[200]*(len(house))
        ss=copy.deepcopy(s)
        while ss:
            r1,c1=ss.popleft()
            for i in range(len(house)):
                r2,c2=house[i][0],house[i][1]
                dp[i]=min(dp[i],abs(r1-r2)+abs(c1-c2))    
        d.append(sum(dp))
        return
    for i in chicken:
        if i in s:
            continue
        if len(s)==0:
            s.append(i)
            f()
            s.pop()
        else:
            if i>s[-1]:
                s.append(i)
                f()
                s.pop()

f()
print(min(d))