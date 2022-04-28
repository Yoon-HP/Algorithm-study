import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
def post_order(start,end):
    if start>end:
        return
    root=pre_order[start]
    index=start+1
    
    while index<=end:
        if pre_order[index]>root:
            break
        index+=1
    post_order(start+1,index-1)
    post_order(index,end)
    print(root)
pre_order=[]
while True:
    try:
        pre_order.append(int(input()))
    except:
        break
post_order(0,len(pre_order)-1)