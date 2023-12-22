# 3197번 백조의 호수
from collections import deque
import sys
input=sys.stdin.readline

R, C = map(int, input().strip().split())

Map = []

L_position = []

start_point = []

visit = [[float("inf") for _ in range(C)] for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(R):
    row = list(input().strip())
    Map.append(row)
    for j in range(C):
        if row[j] == "L":
            L_position.append([i, j])
            visit[i][j] = 0
            start_point.append([i, j, 0])
            continue
        if row[j] == ".":
            start_point.append([i, j, 0])
            # 물은 0
            visit[i][j] = 0

queue = deque(start_point)
while queue:
    x, y, day = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue

        # 얼음부분만 신경쓰면됨
        if Map[nx][ny] == "X":
            if visit[nx][ny] > day + 1:
                visit[nx][ny] = day + 1
                queue.append([nx, ny, day + 1])

check_ans = -1
for i in range(R):
    for j in range(C):
        check_ans = max(check_ans, visit[i][j])


def bfs_search(value):
    global Map, visit, dx, dy, L_position
    global R, C

    # value을 기준으로 도달이 가능한지 파악
    end_x, end_y = L_position[1]
    queue = deque([L_position[0]])

    check_visit = [[False for _ in range(C)] for _ in range(R)]

    # 처음 출발지점
    check_visit[L_position[0][0]][L_position[0][1]]=True

    flag = False
    while queue:
        x, y = queue.popleft()

        if end_x==x and end_y==y:
            # 도달한 경우
            return True
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            
            if check_visit[nx][ny]:
                continue
            
            if visit[nx][ny] > value:
                continue
            
            queue.append([nx,ny])
            check_visit[nx][ny]=True

    return False


# 이분탐색 진행
low = 0
high = check_ans

while low<high:
    mid=(low+high)//2
    if bfs_search(mid):
        high=mid
    else:
        low=mid+1

print(low)