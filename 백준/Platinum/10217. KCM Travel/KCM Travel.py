def ans():
    N,M,K=map(int,input().split())
    Map=[[] for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d=map(int,input().split())
        Map[u].append([v,c,d])
    d=[[float('inf')]*(M+1) for _ in range(N+1)]
    # 1번 노드에서 출발하므로 비용을 0으로 초기화
    d[1][0]=0
    for i in range(M+1):
        for j in range(1,N+1):
            if d[j][i]!=float('inf'):
                for v,c,d_ in Map[j]:
                    if i+c<=M:
                        d[v][i+c]=min(d[v][i+c],d[j][i]+d_)
    result=min(d[N])
    if result==float('inf'):
        print("Poor KCM")
    else:
        print(result)
T=int(input())
for _ in range(T):
    ans()