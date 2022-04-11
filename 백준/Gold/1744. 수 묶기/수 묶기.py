#1744번 수 묶기
import sys
input=sys.stdin.readline
N=int(input())
A=[]
B=[]
for _ in range(N):
    temp=int(input())
    if temp>0:
        A.append(temp)
    else:
        B.append(temp)
result=0
A.sort(reverse=True)
B.sort()
check=[False]*N
if len(B)>=2:
    for i in range(len(B)-1):
        if check[i]:
            continue
        else:
            if B[i]*B[i+1]>B[i]+B[i+1]:
                result+=B[i]*B[i+1]
                check[i+1]=True
                check[i]=True
if len(A)>=2:
    for i in range(len(A)-1):
        if check[len(B)+i]:
            continue
        else:
            if A[i]*A[i+1]>A[i]+A[i+1]:
                result+=A[i]*A[i+1]
                check[len(B)+i]=True
                check[len(B)+i+1]=True
for i in range(N):
    if i<len(B):
        if not check[i]:
            result+=B[i]
    else:
        if not check[i]:
            result+=A[i-len(B)]
print(result)
            
    
    