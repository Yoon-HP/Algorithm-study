def solution(s):
    Min=float('inf')
    Max=float('-inf')
    for check in s.split():
        check=int(check)
        Min=min(Min,check)
        Max=max(Max,check)
    answer = f'{Min} {Max}'
    return answer