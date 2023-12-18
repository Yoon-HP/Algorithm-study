# 숨바꼭질 4

from collections import deque

N, K = map(int, input().split())


# 처음위치, 초,
queue = deque([[N, 0]])

visit = [-1] * 100001

visit[N] = 0
ans_sec = 0
while queue:
    pos, sec = queue.popleft()

    if pos == K:
        ans_sec = sec
        break

    for n_pos in (pos-1,pos+1,pos*2):
        if n_pos < 0 or n_pos > 100000:
            continue
        if visit[n_pos] != -1:
            continue
        queue.append([n_pos, sec + 1])
        visit[n_pos] = sec + 1


temp = ans_sec - 1
PathTrack = [K]

# 어떤 시간대에 방문했는지도 고려해야함
while temp > -1:
    for nk in (K - 1, K + 1, K // 2):
        if nk < 0 or nk > 100000:
            continue
        if visit[nk] == temp:
            PathTrack.append(nk)
            K = nk
            temp -= 1
            break

print(ans_sec)
print(*PathTrack[::-1])