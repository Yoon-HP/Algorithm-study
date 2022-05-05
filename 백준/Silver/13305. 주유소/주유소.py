n=int(input())
length=list(map(int,input().split()))
price=list(map(int,input().split()))
result=0
point=0
for i in range(len(length)):
    if price[point]<=price[i]:
        result+=price[point]*length[i]
    else:
        point=i
        result+=price[point]*length[i]
        
print(result)