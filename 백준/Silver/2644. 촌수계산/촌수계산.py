import collections
import sys
input=sys.stdin.readline

q=collections.deque([])

n=int(input())
u,v=map(int,input().split())
m=int(input())
relation=[[] for _ in range(n+1)]
for _ in range(m):
    parent,child=map(int,input().split())
    relation[parent].append(child)
    relation[child].append(parent)
    
q.append([v,0])
visited=[False]*(n+1)
flag=False
while q:
    key,cnt=q.popleft()
    visited[key]=True
    for i in relation[key]:
        if i==u:
            print(cnt+1)
            flag=True
            q=collections.deque([])
            break
        else:
            if not visited[i]:
                q.append([i,cnt+1])
    
if not flag:
    print(-1)