from collections import deque
def solution(n, computers):
    answer = 0
    visit=[False]*(n)
    for i in range(n):
        if not visit[i]:
            answer+=1
            q=deque([i])
            visit[i]=True
            while q:
                cur=q.popleft()
                for adj in range(n):
                    if computers[cur][adj]==1:
                        if not visit[adj]:
                            visit[adj]=True
                            q.append(adj)
    return answer