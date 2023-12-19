# 확장 게임
from collections import deque
import sys
input=sys.stdin.readline

N, M, P = map(int, input().strip().split())

Map = []

# player 성 위치 (라운드별로 계속 업데이트 해야함) << 새롭게 추가된 친구들에 대해서만 확인하면 되긴함.
player = [[] for _ in range(P + 1)]
Si = [""] + list(map(int, input().strip().split()))
visit = [[False for _ in range(M)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    row = list(input().strip())
    Map.append(row)

    for j in range(len(row)):
        if row[j] != "." and row[j] != "#":
            player[int(row[j])].append([i, j, 0])
            # 이미 성이 존재하므로
            visit[i][j] = True

# 모든 플레이어가 더 이상 확장할 수 없을 때 종료
EndFlag = 1

while True:
    if EndFlag == 0:
        break
    # 라운드 시작
    EndFlag = 0

    for number in range(1, P + 1):
        queue = deque(player[number])
        # Si[number]
        # print(f"player: {number}")
        # print(queue)
        temp = []
        while queue:
            x, y, s = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                # 조건 잘보기
                if Map[nx][ny] != "." or visit[nx][ny]:
                    continue

                if s < Si[number]:
                    Map[nx][ny] = str(number)
                    visit[nx][ny] = True
                    temp.append([nx, ny, 0])
                    #player[number].append([nx, ny, 0])
                    queue.append([nx, ny, s + 1])
                    EndFlag += 1
                    
        # 다음 라운드에서 bfs을 돌릴 친구 
        player[number]=temp

# print(Map)
ans=[0]*(P+1)
for i in range(N):
    for j in range(M):
        if Map[i][j]!='.' and Map[i][j]!='#':
            ans[int(Map[i][j])]+=1

print(*ans[1:])