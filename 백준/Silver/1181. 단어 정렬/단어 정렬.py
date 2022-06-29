import sys
input=sys.stdin.readline

N=int(input())
word=[[str(i)] for i in range(51)]
for _ in range(N):
    check=input().strip()
    word[len(check)].append(check)
    
for i in word:
    temp=set(i)
    temp=list(temp)
    temp.sort()
    for j in range(1,len(temp)):
        print(temp[j])

