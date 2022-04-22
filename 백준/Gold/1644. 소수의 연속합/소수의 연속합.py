N=int(input())
prime=[]
A=[True]*(N+1)
for i in range(2,int((N+1)**0.5)+1):
    if A[i]:
        for j in range(2*i,N+1,i):
            A[j]=False
            
for i in range(2,N+1):
    if A[i]:
        prime.append(i)
L=0
cnt=0
Sum=0
for i in range(len(prime)):
    Sum+=prime[i]
    if Sum==N:
        cnt+=1
    elif Sum>N:
        while True:
            if Sum-prime[L]>=N:
                Sum-=prime[L]
                L+=1
            elif Sum==N:
                cnt+=1
                break
            else:
                break               
if cnt:
    print(cnt)
else:
    print(0)