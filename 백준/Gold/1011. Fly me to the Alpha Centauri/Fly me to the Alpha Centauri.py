import math
def opt(X,Y):
    length=Y-X
    n=str(math.trunc(length**(1/2)))
    if length>int(n)+int(n)**2:
        return 2*int(n)+1
    
    elif length==int(n)**2:
        return 2*int(n)-1
    
    elif length>int(n)**2 and length<=int(n)+int(n)**2:
        return 2*int(n)
    if length < 4:
        return length
    
N=int(input())
A=[]
for _ in range(N):
    X,Y=map(int,input().split())
    A.append(opt(X,Y))
    
for i in A:
    print(i)