import sys
input=sys.stdin.readline
N,M=map(int,input().split())
E=[[0]*(M+2) for i in range(N+2)]
m=[[0]*(M+2) for i in range(N+2)]
S_index=[]
for i in range(1,N+1):
    row='X'+input()+'X'
    for j in range(1,M+1):
        if row[j]=='E':
            m[i][j]=m[i-1][j]+m[i][j-1]-m[i-1][j-1]
            E[i][j]=E[i-1][j]+E[i][j-1]-E[i-1][j-1]+1
        elif row[j]=='M':
            E[i][j]=E[i-1][j]+E[i][j-1]-E[i-1][j-1]
            m[i][j]=m[i-1][j]+m[i][j-1]-m[i-1][j-1]+1
        else:
            S_index.append([i,j])
            E[i][j]=E[i-1][j]+E[i][j-1]-E[i-1][j-1]
            m[i][j]=m[i-1][j]+m[i][j-1]-m[i-1][j-1]
count=0
d=10**9+7
for i in S_index:
    u,v=i[0],i[1]
    count=count+E[u][v]*(m[N][M]-m[N][v-1]-m[u-1][M]+m[u-1][v-1])

print(count%d)