def solution(s):
    s=s.lower()
    
    flag=1
    answer=''
    for i in range(len(s)):
        if flag and s[i]!=' ':
            answer+=s[i].upper()
            flag=0
            continue
            
        if s[i]==' ' and flag==0:
            flag=1
            
        answer+=s[i]
        

    
    return answer