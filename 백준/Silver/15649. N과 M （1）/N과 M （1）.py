import itertools
N,M=map(int,input().split())
A=[]
for i in range(1,N+1):
    A.append(i)
B=[]
for i in itertools.permutations(A,M):
    B.append(list(i))
for i in B:
    for j in i:
        print(j,end=' ')
    print()