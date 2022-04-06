# 14938번 서강그라운드
n,m,r=map(int,input().split())

item=[0]+list(map(int,input().split()))

D=[[0]*(n+1) for _ in range(n+1)]

cost=[[float('inf')]*(n+1) for _ in range(n+1)]

#무방향 그래프!
for i in range(r):
    i,j,c=map(int,input().split())
    cost[i][j]=min(cost[i][j],c)
    cost[j][i]=min(cost[j][i],c)
    
for i in range(n+1):
    for j in range(n+1):
        if i==j:
            cost[i][j]=0
        
#k=0일때
for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j]=cost[i][j]
        
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])
            
item_cnt=[]
for i in range(1,n+1):
    temp=0
    for j in range(1,len(D[i])):
        if D[i][j]<=m:
            temp+=item[j]
    item_cnt.append(temp)
    
print(max(item_cnt))