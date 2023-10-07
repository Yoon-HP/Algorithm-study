L,C=map(int,input().split())

words=input().split()

words.sort()
a=set(['a','i','e','o','u'])

visited=[False]*(C)

s=[]
def code(cnt1,cnt2):
    if len(s)==L:
        if cnt1>=1 and cnt2>=2:
            print(''.join(s))
            return
        return
    
    for i in range(C):
        if len(s)==0:
            s.append(words[i])
            if words[i] in a:
                cnt1+=1
            else:
                cnt2+=1
            visited[i]=True
            code(cnt1,cnt2)
            visited[i]=False
            check=s[-1]
            if check in a:
                cnt1-=1
            else:
                cnt2-=1
            s.pop()
        else:
            if not visited[i] and s[-1]<words[i]:
                s.append(words[i])
                if words[i] in a:
                    cnt1+=1
                else:
                    cnt2+=1
                visited[i]=True
                code(cnt1,cnt2)
                visited[i]=False
                check=s[-1]
                if check in a:
                    cnt1-=1
                else:
                    cnt2-=1
                s.pop()
code(0,0)            
        