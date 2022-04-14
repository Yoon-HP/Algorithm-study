import collections
import sys
input=sys.stdin.readline

N=int(input())
Number=list(map(int,input().split()))

dp_dict=collections.defaultdict(set)

table=collections.defaultdict(set)

for i in range(N):
    if not table[Number[i]]:
        # index 저장
        table[Number[i]].add(i)
    else:
        for j in table[Number[i]]:
            if i-j<=2:
                dp_dict[j].add(i)
            else:
                if i-1 in dp_dict[j+1]:
                    dp_dict[j].add(i)
        table[Number[i]].add(i)
        
M=int(input())
for _ in range(M):
    S,E=map(int,input().split())
    S-=1
    E-=1
    if S==E:
        print(1)
    else:
        if E in dp_dict[S]:
            print(1)
        else:
            print(0)
