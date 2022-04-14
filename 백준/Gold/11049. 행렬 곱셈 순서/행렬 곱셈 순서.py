import sys
input=sys.stdin.readline

N=int(input())
q=[]
for i in range(N):
    if i==0:
        r,c=map(int,input().split())
        q.append(r)
        q.append(c)
    else:
        r,c=map(int,input().split())
        q.append(c)

#n=3 >인덱스 0 1 2 3 을 사용할 것
n=len(q)-1

m=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    m[i][i]=0

# j~k까지 j~h, h+1~k
for i in range(2,n+1):
    for j in range(1,n-i+2):
        k=j+i-1
        m[j][k]=float('inf')
        for h in range(j,k):
            key=m[j][h]+m[h+1][k]+q[j-1]*q[h]*q[k]
            if key<m[j][k]:
                m[j][k]=key
                
print(m[1][-1])