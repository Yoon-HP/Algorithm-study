import sys
input=sys.stdin.readline

T=int(input())
prime=[True]*(10001)
prime[1]=False;prime[0]=False
for i in range(2,int((10001)**(1/2))+1):
    if prime[i]:
        for j in range(2*i,10001,i):
            prime[j]=False

for _ in range(T):
    n=int(input())
    result=float('inf')
    L=0
    for i in range(2,int(n/2)+1):
        if prime[i] and prime[n-i]:
            if abs(2*i-n)<result:
                L=i
    print(L,n-L)