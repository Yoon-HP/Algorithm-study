def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    
    while A:
        if A[-1]>B[-1]:
            answer+=A[-1]*B[0]
            B.pop(0)
            A.pop()
        elif A[-1]<=B[-1]:
            answer+=A[0]*B[-1]
            B.pop()
            A.pop(0)
    
    return answer