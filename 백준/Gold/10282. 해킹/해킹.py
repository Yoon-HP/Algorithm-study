import heapq
import sys
input=sys.stdin.readline

def ans():
    n,d,c=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    visit=[False]*(n+1)
    for _ in range(d):
        a,b,s=map(int,input().split())
        graph[b].append([a,s])
    cnt=0
    time=0
    # time,start
    h=[[0,c]]
    sttime=[float('inf')]*(n+1)
    sttime[c]=0
    while h:
        t,a=heapq.heappop(h)
        if not visit[a]:
            cnt+=1
            visit[a]=True
        if sttime[a]<t:
            continue
        for b,s in graph[a]:
            temp_t=t+s
            if temp_t<sttime[b]:
                sttime[b]=temp_t
                heapq.heappush(h,[temp_t,b])
            
    for j in sttime:
        if j!=float('inf'):
            time=max(time,j)
                
    print(f'{cnt} {time}')

T=int(input())
for _ in range(T):
    ans()