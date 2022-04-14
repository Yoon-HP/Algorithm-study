import sys
n=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
a=[-1]*n
st=[]

st.append(0)
for i in range(1,n):
    while st and A[st[-1]]<A[i]:
        a[st.pop()]=A[i]
    st.append(i)
print(*a)