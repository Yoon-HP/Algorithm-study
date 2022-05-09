N=int(input())
arr=[[] for _ in range(N)]

Map=[]
for _ in range(5):
    Map.append(list(input()))

rule=[[1],[1,4],[],[1,2,3,7],[0,1,2,3,4,5,6,7,8,9],[5,6],[1,7],
      [0,1,7],[],[1,3,4,5,7,9],[0,1,2,3,4,5,6,7,8,9],[2],[1,4,7],
      [1,4,7],[]]
low_bound=0
for k in range(N):
    possible=set([0,1,2,3,4,5,6,7,8,9])
    tem=[]
    for i in range(5):
        for j in range(3):
            if Map[i][low_bound+j]=="#":
                tem=rule[i*3+j]+tem
    low_bound+=4
    arr[k]=list(possible.difference(set(tem)))

flag=1
for i in arr:
    if len(i)==0:
        flag=0
if flag:
    result=0
    temp_sum=[0 for _ in range(N)]
    for i in range(N):
        for j in range(len(arr[i])):
            temp_sum[i]+=arr[i][j]
    for i in range(N):
        result*=10
        result+=temp_sum[i]/len(arr[i])
    print(result)
    
else:
    print(-1)