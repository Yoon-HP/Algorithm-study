N,r,c=map(int,input().split())
ans=0
# 결국 r,c를 0,0으로 옮기는 과정을 거쳐가며 개수를 세면 됨.
# 1/4로 주어진 table을 계속해서 분할해 가면서 답을 찾아 나감.
# 규칙을 찾고 이를 일반화해서 표현 하면 됨.
while N!=0:
    N-=1
    if r<2**N and c<2**N:
        ans+=(2**N)*(2**N)*0
    elif r<2**N and c>=2**N:
        ans+=(2**N)*(2**N)*1
        c-=(2**N)
    elif r>=2**N and c<2**N:
        ans+=(2**N)*(2**N)*2
        r-=(2**N)
    else:
        ans+=(2**N)*(2**N)*3
        r-=(2**N)
        c-=(2**N)
        
print(ans)
        