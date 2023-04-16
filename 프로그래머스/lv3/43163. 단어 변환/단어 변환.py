from collections import deque
def solution(begin, target, words):
    answer=0
    check={words[i]:0 for i in range(len(words))}
    temp_list=list(check.keys())
    
    # 종료 조건
    if target not in temp_list:
        return 0
    
    if begin not in temp_list:
        check[begin]=0
        
    q=deque([begin])
    while q:
        cur=q.popleft()
        for i in temp_list:
            if check[i]:
                continue
            cnt=0
            for j in range(len(i)):
                if cur[j]!=i[j]:
                    cnt+=1
            if cnt==1:
                check[i]=check[cur]+1
                q.append(i)
                
    if check[target]:
        answer=check[target]
    else:
        answer=0
        
    return answer