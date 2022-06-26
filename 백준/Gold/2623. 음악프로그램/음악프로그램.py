import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int,input().split())
in_degree=[0]*(N+1)
graph=[[] for _ in range(N+1)]

for _ in range(M):
    temp=list(map(int,input().split()))
    for i in range(1,len(temp)-1):
        in_degree[temp[i+1]]+=1
        graph[temp[i]].append(temp[i+1])

ans=[]
q=deque()
cnt=0
for i in range(1,N+1):
    if in_degree[i]==0:
        q.append(i)
while q:
    current = q.popleft()
    ans.append(current)
    cnt+=1
    for x in graph[current]:
        in_degree[x] -= 1

        if in_degree[x] == 0:
            q.append(x)

if cnt==N:
    for i in ans:
        print(i)
else:
    print(0)