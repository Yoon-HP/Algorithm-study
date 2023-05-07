def solution(cap, n, deliveries, pickups):
    
    cap=cap
    n=n
    
    
    non_zero_deliveries=[]
    non_zero_pickups=[]
    for i in range(n):
        if deliveries[i]:
            non_zero_deliveries.append(i)
        if pickups[i]:
            non_zero_pickups.append(i)
            
    answer=0
    cur_index=n-1
    while cur_index>-1:
        if deliveries[cur_index]==0 and pickups[cur_index]==0:
            cur_index-=1
        else:
            answer+=(cur_index+1)*2
            
            cur_d=0
            cur_p=0
            
            # d
            while True:
                if len(non_zero_deliveries)==0:
                    break
                if cur_d+deliveries[non_zero_deliveries[-1]]<=cap:
                    cur_d+=deliveries[non_zero_deliveries[-1]]
                    deliveries[non_zero_deliveries[-1]]=0
                    non_zero_deliveries.pop()
                else:
                    deliveries[non_zero_deliveries[-1]]-=cap-cur_d
                    break
            # p
            while True:
                if len(non_zero_pickups)==0:
                    break
                if cur_p+pickups[non_zero_pickups[-1]]<=cap:
                    cur_p+=pickups[non_zero_pickups[-1]]
                    pickups[non_zero_pickups[-1]]=0
                    non_zero_pickups.pop()
                else:
                    pickups[non_zero_pickups[-1]]-=cap-cur_p
                    break
    return answer