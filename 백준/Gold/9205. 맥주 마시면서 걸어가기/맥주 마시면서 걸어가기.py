# 맥주 마시면서 걸어가기
from collections import deque
import sys
input=sys.stdin.readline

t=int(input())


for _ in range(t):
    n=int(input())
    Map=[]
    home=list(map(int,input().split()))
    Map.append(home)
    for _ in range(n):
        Map.append(list(map(int,input().split())))
        
    end=list(map(int,input().split()))
    Map.append(end)
    
    # index 0 << start, n+1 << end
    graph=[[] for _ in range(n+2)]
    
    for i in range(n+2):
        for j in range(i+1,n+2):
            if i!=j:
                dist=abs(Map[i][0]-Map[j][0])+abs(Map[i][1]-Map[j][1])
                if dist<=1000:
                    graph[i].append(j)
                    graph[j].append(i)
                    
    visit=[False]*(n+2)
    
    q=deque([0])
    visit[0]=True
    flag=False
    while q:
        cur=q.popleft()
        if cur==n+1:
            print("happy")
            flag=True
            break
        for adj in graph[cur]:
            
            # 만약 방문 했다면!
            if visit[adj]:
                continue
            visit[adj]=True
            q.append(adj)
    
    if not flag:
        print("sad")