# 9238번 열쇠
from collections import deque
import sys
input=sys.stdin.readline

T = int(input().strip())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(T):
    h, w = map(int, input().strip().split())

    # 현재 위치에서 도달 가능한 알파벳 위치
    CheckAlpha = {}
    # 열쇠가 존재하는지

    Map = []

    # 맨 처음 queue에 넣어 확인해 볼 곳
    StartPoint = []
    ans = 0
    key_set = set()
    for i in range(h):
        row = list(input().strip())
        Map.append(row)

        for j in range(w):
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                # 가장자리 중 벽이 아닌 경우
                if row[j] != "*":
                    StartPoint.append([i, j])

                if ord("a") <= ord(row[j]) <= ord("z"):
                    key_set.add(row[j])

    key = input().strip()
    for i in key:
        key_set.add(i)

    visit = [[-1 for _ in range(w)] for _ in range(h)]

    # 초기 상태 세팅

    queue = deque([])

    for x, y in StartPoint:
        if Map[x][y] == ".":
            visit[x][y] = 1
            queue.append([x, y])
            continue
        if Map[x][y].lower() in key_set:
            visit[x][y] = 1
        else:
            if Map[x][y] == "$":
                ans += 1
            else:
                # 나중에 열쇠가 발견되면 그때 다시 queue에 넣고 bfs 돌리기
                visit[x][y] = 2
                if Map[x][y] in CheckAlpha:
                    CheckAlpha[Map[x][y]].append([x, y])
                else:
                    CheckAlpha[Map[x][y]] = [[x, y]]
                continue
        visit[x][y] = 1
        queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            # 1은 다시 볼 필요가 없는 지점 + 벽은 확인 X
            if visit[nx][ny] == 1 or Map[nx][ny] == "*":
                continue

            # 문서를 발견한 경우
            if Map[nx][ny] == "$":
                ans += 1
                visit[nx][ny] = 1
                queue.append([nx, ny])

            # 열쇠를 발견한 경우
            if ord("a") <= ord(Map[nx][ny]) <= ord("z"):
                visit[nx][ny] = 1
                if Map[nx][ny] not in key_set:
                    key_set.add(Map[nx][ny])

                # 키가 존재하지 않을수도 있음
                if Map[nx][ny].upper() in CheckAlpha:
                    while CheckAlpha[Map[nx][ny].upper()]:
                        a, b = CheckAlpha[Map[nx][ny].upper()].pop()
                        visit[a][b] = 1
                        queue.append([a, b])

                queue.append([nx, ny])
                continue

            # 문을 발견한 경우
            if ord("A") <= ord(Map[nx][ny]) <= ord("Z"):
                if Map[nx][ny].lower() in key_set:
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
                else:
                    # 나중에 열쇠가 생기면 확인
                    visit[nx][ny] = 2

                    if Map[nx][ny] in CheckAlpha:
                        CheckAlpha[Map[nx][ny]].append([nx, ny])
                    else:
                        CheckAlpha[Map[nx][ny]] = [[nx, ny]]
                continue

            # 일반 통로
            visit[nx][ny] = 1
            queue.append([nx, ny])

    print(ans)