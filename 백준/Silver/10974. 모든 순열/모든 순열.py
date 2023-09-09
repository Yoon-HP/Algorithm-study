N=int(input())
B=[i+1 for i in range(N)]
s=[]
def dfs():
    if len(s)==N:
        print(' '.join(map(str,s)))
    for i in B:
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

dfs()