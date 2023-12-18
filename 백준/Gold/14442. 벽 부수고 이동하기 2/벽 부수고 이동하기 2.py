from collections import deque
import sys
input=sys.stdin.readline

N, M, K = map(int, input().split())
Map = []
for _ in range(N):
    row = list(input())
    Map.append(row)

visit = [[[float("inf") for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# x,y,d,k
queue = deque([[0, 0, 0, 0]])
visit[0][0][0] = 0

flag=True
while queue:
    x, y, d, k = queue.popleft()

    if x==N-1 and y==M-1:
        # 시작하는 칸 추가
        print(d+1)
        flag=False
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 벽인 경우
        if Map[nx][ny] == "1":
            if k >= K:
                continue
            nk = k + 1
        else:
            nk = k
            
        # 이미 방문한 경우라면 pass
        if visit[nx][ny][nk] <= d+1:
            continue
        visit[nx][ny][nk] = d + 1
        queue.append([nx, ny, d + 1, nk])

if flag:
    print(-1)