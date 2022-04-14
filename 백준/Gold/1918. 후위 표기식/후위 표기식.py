st1=list(input())
operator=set(["*","/","(",")","+","-"])
priority_dict={"*":1,"/":1,"+":2,"-":2,"(":3}
st=[]
result=''
for i in st1:
    if i not in operator:
        result+=i
    else:
        if i=="(":
            st.append(i)
        elif i==")":
            while True:
                if st[-1]=="(":
                    st.pop()
                    break
                else:
                    result+=st.pop()
        else:
            if st:
                if priority_dict[st[-1]]>priority_dict[i]:
                    st.append(i)
                else:
                    while True:
                        if st:
                            if priority_dict[st[-1]]<=priority_dict[i]:
                                result+=st.pop()
                            else:
                                st.append(i)
                                break
                        else:
                            st.append(i)
                            break
            else:
                st.append(i)
    
while st:
    if st[-1]!="(":
        result+=st.pop()
    else:
        st.pop()
  
print(result)   