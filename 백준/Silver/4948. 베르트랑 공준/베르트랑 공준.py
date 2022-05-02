import sys
input=sys.stdin.readline

prime=[True]*(123456*2+1)
prime[1]=False;prime[0]=False
for i in range(2,int((123456*2+1)**(1/2))+1):
    if prime[i]:
        for j in range(2*i,123456*2+1,i):
            prime[j]=False
while True:
    n=int(input())
    if n==0:
        break
    cnt=0
    for i in range(n+1,2*n+1):
        if prime[i]:
            cnt+=1
    print(cnt)