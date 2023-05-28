def solution(n, words):
    answer = []
    human=[0]*n
    word_set=set()
    for i in range(len(words)):
        human[i%n]+=1
        if i!=0:
            if words[i-1][-1]!=words[i][0]:
                answer=[i%n+1,human[i%n]]
                break
        
        if words[i] not in word_set:
            word_set.add(words[i])
        else:
            answer=[i%n+1,human[i%n]]
            break
        
    if not answer:
        answer=[0,0]
    return answer