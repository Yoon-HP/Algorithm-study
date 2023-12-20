# 17071번 숨바꼭질 5
from collections import deque

N,K=map(int,input().split())

visit=[float('inf')]*(500001)

# 수빈이 먼저 bfs 돌리기

# 현재 위치, 시간
queue=deque([[N,0]])
visit[N]=0
visit_odd=[float('inf')]*(500001)
while queue:
    cur_N,t=queue.popleft()
    
    for nN in (cur_N+1,cur_N-1,cur_N*2):
        if nN<0 or nN>500000:
            continue
        
        if visit[nN]<=t+1:
            if ((t+1)-visit[nN])%2!=0:
                if visit_odd[nN]>t+1:
                    visit_odd[nN]=t+1
                    queue.append([nN,t+1])
            continue
        visit[nN]=t+1

        queue.append([nN,t+1])
# 동생 위치 확인 n 초 후, K+(n*(n+1))/2

T=0
cur_K=K
ans=float('inf')

# T는 최대 1000 미만
while True:
    if cur_K<=500000:
        # 되돌아서 오는 경우도 고려     
        # 둘의 차가 짝수인 경우
        if (T-visit[cur_K])%2==0 and (T-visit[cur_K])>=0:
            ans=min(ans,T)
        
        # 둘의 차가 홀수인 경우
        if (T-visit_odd[cur_K])%2==0 and (T-visit_odd[cur_K]>=0):
            ans=min(ans,T)
    else:
        break
    T+=1
    cur_K=K+(T*(T+1))//2

if ans!=float('inf'):
    print(ans)
else:
    print(-1)