def solution(s):
    answer = True
    
    l_cnt=0
    for i in s:
        if l_cnt<0:
            return False
        if i=="(":
            l_cnt+=1
        else:
            l_cnt-=1
    if l_cnt:
        return False
    return True