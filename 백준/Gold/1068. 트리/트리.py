import sys
sys.setrecursionlimit(10 ** 9)
n=int(input())
node=list(map(int,input().split()))
del_nd=int(input())
cnt=0

tree=[[]for _ in range(n+2)]
for i in range(n):
    if node[i]==-1:
        tree[n+1].append(i)
    else:
        tree[node[i]].append(i)

def dfs(x):
    global cnt
    if len(tree[x])==0:
        cnt+=1
        return
    for i in range(len(tree[x])):
        if tree[x][i]==del_nd:
            if len(tree[x])==1:
                cnt+=1
        else:
            dfs(tree[x][i])
            
if node[del_nd]==-1:
    print(0)
else:
    dfs(n+1)
    print(cnt)