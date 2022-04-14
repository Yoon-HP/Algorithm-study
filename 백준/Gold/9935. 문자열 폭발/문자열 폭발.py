S=list(input().strip())
bomb=list(input().strip())
st=[]
for i in range(len(S)):
    st.append(S[i])
    if S[i]==bomb[-1] and len(st)>=len(bomb):
        if st[-len(bomb):]==bomb:
            for i in range(len(bomb)):
                st.pop()

if st:
    print(''.join(st))
else:
    print("FRULA")