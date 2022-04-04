# 11404번 플로이드
import sys
input=sys.stdin.readline

N=int(input())
m=int(input())

cost=[[float('inf')]*(N+1) for _ in range(N+1)]
#홀수
D1=[[0]*(N+1) for _ in range(N+1)]
#짝수
D2=[[0]*(N+1) for _ in range(N+1)]

for i in range(m):
    i,j,c=map(int,input().split())
    cost[i][j]=min(cost[i][j],c)
for i in range(N+1):
    for j in range(N+1):
        if i==j:
            cost[i][j]=0

#k=0일때
for i in range(1,N+1):
    for j in range(1,N+1):
        D2[i][j]=cost[i][j]

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if k%2==1:
                D1[i][j]=min(D2[i][j],D2[i][k]+D2[k][j])
            else:
                D2[i][j]=min(D1[i][j],D1[i][k]+D1[k][j])

if N%2==1:
    for i in range(1,N+1):
        for j in range(1,N+1):
            if D1[i][j]==float('inf'):
                D1[i][j]=0
    for i in range(1,N+1):
        print(" ".join(map(str,D1[i][1:])))
else:
    for i in range(1,N+1):
        for j in range(1,N+1):
            if D2[i][j]==float('inf'):
                D2[i][j]=0
    for i in range(1,N+1):
        print(" ".join(map(str,D2[i][1:])))
            

