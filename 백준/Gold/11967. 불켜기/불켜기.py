# 11967번 불켜기
from collections import deque
import sys
input=sys.stdin.readline

N, M = map(int, input().strip().split())

graph = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(M):
    x, y, a, b = map(int, input().strip().split())
    graph[x][y].append([a, b])


# 0은 아직 방문 X, 1은 방문도하고 불도 켜져 있는 상태, 2는 방문은 했지만, 아직 불은 안켜진 상태
visit = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
fire = [[False for _ in range(N + 1)] for _ in range(N + 1)]

ans = 1
queue = deque([[1, 1]])
visit[1][1] = 1
fire[1][1] = True

# 처음 방에서 킬 수 있는 방은 모두 켜기
for a, b in graph[1][1]:
    if not fire[a][b]:
        fire[a][b] = True
        ans+=1

while queue:
    x, y = queue.popleft()

    # 이동하기전에 불을 먼저 켜야함
    for a, b in graph[x][y]:
        if not fire[a][b]:
            fire[a][b] = True
            ans+=1

        # 뒤늦게 불을 켜서 갈 수 있게 된 경우
        if visit[a][b] == 2:
            visit[a][b] = 1
            queue.append([a, b])

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 1 or nx >= (N + 1) or ny < 1 or ny >= (N + 1):
            continue

        # 이미 방문한 곳은 패스
        if visit[nx][ny] != 0:
            continue

        if fire[nx][ny]:
            visit[nx][ny] = 1
            queue.append([nx, ny])
        else:
            visit[nx][ny] = 2

print(ans)