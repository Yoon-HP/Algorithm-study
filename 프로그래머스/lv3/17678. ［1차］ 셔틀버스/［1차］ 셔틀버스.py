import traceback

def solution(n, t, m, timetable):
    answer = ''
    
    # timetable 변형
    timetable.sort()
    len_table=len(timetable)
    
    cur_time='09:00'
    check_index=0
    cur_answer="00:00"
    for check in range(n):
        cur_m=0
        while cur_m<m:
            
            try:            
                if check_index<len_table:
                    if timetable[check_index]<=cur_time:
                        cur_m+=1
                        cur_answer=max(cur_answer,timetable[check_index])
                        check_index+=1
                    else:
                        cur_answer=max(cur_answer,cur_time)
                        break
                else:
                    cur_answer=max(cur_answer,cur_time)
                    break
            except:
                print("???")
                
                
        if cur_m==m:
            # -1분 구현
            temp=""
            if cur_answer[3:]=="00":
                # hour 구하기
                if cur_answer[0]=="0":
                    hour=int(cur_answer[1])
                else:
                    hour=int(cur_answer[:2])
                hour-=1
                
                if hour<10:
                    temp+="0"+str(hour)+":59"
                else:
                    temp+=str(hour)+":59"
                    
            else:
                if cur_answer[3]=="0":
                    temp+=cur_answer[:3]+"0"+str(int(cur_answer[4])-1)
                else:
                    if int(cur_answer[3:])-1<10:
                        temp+=cur_answer[:3]+"0"+str(int(cur_answer[3:])-1)
                    else:
                        temp+=cur_answer[:3]+str(int(cur_answer[3:])-1)
                
            #print(temp)
            cur_answer=temp
        
        # 현재 시간 갱신
        if cur_time[0]=="0":
            hour=int(cur_time[1])
        else:
            hour=int(cur_time[:2])
        
        if cur_time[3]=="0":
            minute=int(cur_time[4])
        else:
            minute=int(cur_time[3:])
        
        
        if minute+t>=60:
            hour+=1
            minute=minute+t-60
        else:
            minute=minute+t
        
        temp=""
        if hour<10:
            temp+="0"+str(hour)+":"
        else:
            temp+=str(hour)+":"
        
        if minute<10:
            temp+="0"+str(minute)
        else:
            temp+=str(minute)
        
        #print(temp)
        cur_time=temp
        
    return cur_answer