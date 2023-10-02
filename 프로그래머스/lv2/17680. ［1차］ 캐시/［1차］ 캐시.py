import traceback
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    try:
        q=deque([])
        for city in cities:
            city=city.lower()
            if city in q:
                if cacheSize==0:
                    answer+=5
                    continue
                answer+=1
                # 기존 친구 제거
                q.remove(city)
            else:
                if len(q)>=cacheSize and len(q)!=0:
                    q.popleft()
                answer+=5
            q.append(city)
    except:
        err_msg = traceback.format_exc()
        print("1", err_msg)
    return answer