a,b=map(int,input().split())

A=set(list(map(int,input().split())))

B=set(list(map(int,input().split())))

temp1=A-B
temp2=B-A
result=temp1|temp2
print(len(list(result)))