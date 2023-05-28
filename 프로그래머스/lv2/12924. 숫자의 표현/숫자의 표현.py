def solution(n):
    answer = 0
    for i in range(1,n+1):
        init=i
        temp=n
        while True:
            temp-=init
            if temp==0:
                answer+=1
            elif temp<0:
                break
            else:
                init+=1
    return answer