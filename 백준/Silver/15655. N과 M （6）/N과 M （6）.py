n,m=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
s=[]
def f():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in A:
        if i in s:
            continue
        if len(s)==0:
            s.append(i)
            f()
            s.pop()
        else:
            if i>s[-1]:
                s.append(i)
                f()
                s.pop()
f()