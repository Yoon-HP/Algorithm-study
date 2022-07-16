import heapq
import sys
input=sys.stdin.readline

N=int(input())
h=[]
ans=0
for i in range(N):
    heapq.heappush(h,int(input()))

cnt=N
while cnt>1:
    first=heapq.heappop(h)
    second=heapq.heappop(h)
    heapq.heappush(h,first+second)
    ans+=first+second
    cnt-=1
    
print(ans)