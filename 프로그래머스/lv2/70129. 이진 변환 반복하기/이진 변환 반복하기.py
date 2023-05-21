def solution(s):
    answer = [0,0]
    while True:
        if s=="1":
            break
        answer[0]+=1
        s=list(s)
        temp=0
        for i in s:
            if i=='0':
                answer[1]+=1
            else:
                temp+=1
        s=""
        while temp:
            s+=str(temp%2)
            temp=int(temp/2)
        s=s[::-1]
            
    return answer