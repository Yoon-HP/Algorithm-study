import collections 
import sys
input=sys.stdin.readline
#다시 풀어보기

N=int(input())

graph=[[] for i in range(N+1)]
visited=[False]*(N+1)

for i in range(N-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

User=list(map(int,input().split()))
child=collections.defaultdict(list)

def bfs(n):
    q=collections.deque([n])
    visited[n]=True
    while q:
        key=q.popleft()
        for i in graph[key]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                child[key].append(i)


if User[0]!=1:
    print(0)
else:
    bfs(1)
    q=collections.deque([1])
    idx=1
    T=True
    while q:
        key=q.popleft()

        a=set(child[key])

        len_a=len(a)
        b=User[idx:idx+len_a]
        q.extend(b)
        b=set(b)
        idx+=len_a

        if a!=b:
            print(0)
            T=False
            break
    
    if T:
        print(1)