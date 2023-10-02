import re
def solution(dartResult):
    answer = 0
    
    rule={'S':1, 'D':2, 'T':3}
    score=re.findall(r'[0-9]+',dartResult)
    bonus=re.findall(r'[a-zA-Z]', dartResult)
    option=['','','']
    
    cnt=-1
    for i in dartResult:
        if i.isalpha():
            cnt+=1
            continue
        if i.isdigit():
            continue
        if cnt==0:
            option[cnt]+=i
            continue
        if i=="*":
            option[cnt-1]+=i
            option[cnt]+=i
            continue
        option[cnt]+=i
        
    print(score)
    print(bonus)
    print(option)
    
    for i in range(3):
        temp=int(score[i])**rule[bonus[i]]
        for opt in option[i]:
            if opt=='*':
                temp*=2
            elif opt=='#':
                temp*=-1
        answer+=temp
    
    return answer