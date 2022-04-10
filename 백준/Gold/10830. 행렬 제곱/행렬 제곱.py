N,B=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]

def matrix(A,B):
    n=len(A)
    c=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j]+=A[i][k]*B[k][j]%1000
            c[i][j]=c[i][j]%1000
    return c

def matrix_power(A,B):
    if B==1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j]%=1000
        return A
    if B%2!=0:
        y=matrix_power(A,(B-1)/2)
        return matrix(A,matrix(y,y))
    else:
        y=matrix_power(A,B/2)
        return matrix(y,y)
    
for i in matrix_power(A,B):
    print(' '.join(map(str,i)))