import sys
input=sys.stdin.readline

N,S=map(int,input().split())
Sum=0
arr=list(map(int,input().split()))
flag=0
L=0
Min=float('inf')
for i in range(N):
    Sum+=arr[i]
    if Sum>=S:
        flag=1
        while True:
            if Sum-arr[L]>=S:
                Sum-=arr[L]
                L+=1
            else:
                Min=min(Min,i-L+1)
                break                
if flag:
    print(Min)
else:
    print(0)