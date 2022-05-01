from collections import defaultdict
N=int(input())

arr=list(map(int,input().split()))
parent=defaultdict(int)
parent[0]=-1
start=0
for i in range(1,len(arr)):
    if arr[i]<arr[start]:
        parent[i]=start
    else:
        while (1):
            temp=parent[start]
            if temp==-1:
                parent[i]=-1
                break
            if arr[temp]>arr[i]:
                parent[i]=temp
                break
            else:
                start=temp
    start=i
for i in range(N):
    print(parent[i]+1,end=" ")