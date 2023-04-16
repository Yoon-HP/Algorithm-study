def solution(scores):
    answer = 0
    check=scores[0]
    n=len(scores)
    scores.sort(reverse=True)
    cur_two_max=scores[0][1]
    prev_two_max=scores[0][1]
    cur_one_max=scores[0][0]
    check_person=[True]*n
    for i in range(n):
        if scores[i][0]!=scores[0][0]:
            if scores[i][0]==cur_one_max:
                    if prev_two_max>scores[i][1]:
                        check_person[i]=False
                    else:
                        cur_two_max=max(cur_two_max,scores[i][1])
            else:
                prev_two_max=max(prev_two_max,cur_two_max)
                cur_one_max=scores[i][0]
                if scores[i][1]<cur_two_max:
                    check_person[i]=False
                cur_two_max=max(cur_two_max,scores[i][1])
    temp=[]
    flag=0
    for i in range(n):
        if check_person[i]:
            temp.append(scores[i][0]+scores[i][1])
            if check[0]==scores[i][0] and check[1]==scores[i][1]:
                flag=1
                
    temp.sort(reverse=True)
    if flag:
        ck=check[0]+check[1]
        cnt=1
        for i in range(n):
            if temp[i]==ck:
                return cnt
            cnt+=1
    else:
        answer=-1
    return answer