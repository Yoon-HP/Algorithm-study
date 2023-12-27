import heapq
import sys
from collections import deque

#input = sys.stdin.readline
W, H = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

razer = []
Map = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if Map[i][j] == "C":
            razer.append([i, j])

heap = [[-1] + razer[0] + [-1]]

# 횟수, dir 저장
visit = [
    [[float("inf"), [False, False, False, False]] for _ in range(W)] for _ in range(H)
]

visit[razer[0][0]][razer[0][1]][0] = -1

queue = deque([[-1, razer[0][0], razer[0][1], -1]])
while queue:
    cnt, u, v, dir = queue.popleft()
    for i in range(4):
        a = u + dx[i]
        b = v + dy[i]

        if a < 0 or a >= H or b < 0 or b >= W:
            continue

        if Map[a][b] == "*":
            continue

        if i != dir:
            if cnt + 1 < visit[a][b][0]:
                queue.append(([cnt + 1, a, b, i]))
                visit[a][b][0] = cnt + 1
                visit[a][b][1][i] = True
            elif cnt + 1 == visit[a][b][0] and not visit[a][b][1][i]:
                visit[a][b][1][i] = True
                queue.append(([cnt + 1, a, b, i]))
        else:
            if cnt < visit[a][b][0]:
                queue.append([cnt, a, b, i])
                visit[a][b][0] = cnt
                visit[a][b][1][i] = True
            elif cnt == visit[a][b][0] and not visit[a][b][1][i]:
                visit[a][b][1][i] = True
                queue.append(([cnt, a, b, i]))

print(visit[razer[1][0]][razer[1][1]][0])