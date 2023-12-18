# 숨바꼭질 4

from collections import deque

N, K=map(int,input().split())


# 처음위치, 초, Path
queue=deque([[N,0,f"{N}"]])

visit=[False]*100001


while queue:
    pos,sec,path=queue.popleft()
    
    if pos==K:
        print(len(path.split())-1)
        print(path)
        break

    for i in range(3):
        if i==0:
            n_pos=pos-1
        elif i==1:
            n_pos=pos+1
        elif i==2:
            n_pos=pos*2
    
        if n_pos<0 or n_pos>100000:
            continue
        if visit[n_pos]:
            continue
        
        queue.append([n_pos,sec+1,path+f" {n_pos}"])
        visit[n_pos]=True