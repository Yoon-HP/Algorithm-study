import sys
input=sys.stdin.readline

n=int(input())
cases=list(map(int,input().split()))
lis=[-float('inf')]
# 각 인덱스에 해당하는 수가 어떤 부분수열의 마지막 수 인지 표현
d=[0]*n

for i in range(len(cases)):
    if lis[-1]<cases[i]:
        lis.append(cases[i])
        d[i]=len(lis)-1
    else:
        left=0
        right=len(lis) 
        while left<right:
            mid=(right+left)//2
            if lis[mid]<cases[i]:
                left=mid+1
            else:
                right=mid
        d[i]=right
        lis[right]=cases[i]
        
print(len(lis)-1)

length=len(lis)-1
ans=[]
for i in range(n-1,-1,-1):
    if d[i]==length:
        ans.append(cases[i])
        length-=1
ans.reverse()
print(*ans)