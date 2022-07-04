from collections import deque 

n,k=map(int,input().split())
visited=[0]*100001
q=deque([[n,0]])
while q:
    p,t=q[0][0],q[0][1]
    if p==k:
        print(t)
        break
    q.popleft()
    visited[p]=1
    if p-1>=0 and visited[p-1]==0:
        q.append([p-1,t+1])
    if p+1 <=100000 and visited[p+1]==0:
        q.append([p+1,t+1])
    if p*2 <=100000 and visited[p*2]==0:
        q.appendleft([p*2,t])