import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N=int(input())
    st=[0]+list(map(int,input().split()))
    visited=[False]*(N+1)
    cnt=0
    for i in range(1,N+1):
        if not visited[i]:
            q=[i]
            visited[i]=True
            while True:
                if not visited[st[q[-1]]]:
                    visited[st[q[-1]]]=True
                    q.append(st[q[-1]])
                else:
                    index=-1
                    for j in range(len(q)):
                        if q[j]==st[q[-1]]:
                            index=j
                            break
                    if index!=-1:
                        cnt+=index
                    else:
                        cnt+=len(q)
                    break
    print(cnt)