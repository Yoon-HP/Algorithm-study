import collections
import sys
input=sys.stdin.readline
n=int(input())
A=list(map(int,input().split()))
B=collections.defaultdict(int)
for i in A:
    B[i]+=1
a=[-1]*n
st=[]

st.append(0)
for i in range(1,n):
    while st and B[A[st[-1]]]<B[A[i]]:
        a[st.pop()]=A[i]
    st.append(i)
print(*a)