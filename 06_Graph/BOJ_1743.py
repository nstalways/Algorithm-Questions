import sys
input = sys.stdin.readline

# 입력
N, M, K = map(int, input().split())
board = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1

# 풀이
"""
그래프 탐색 문제
>> 음식물이 떨어진 좌표에서 상/하/좌/우 탐색을 수행
>> 인접한 음식물의 수를 센다
"""
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False] * (M + 1) for _ in range(N + 1)]

def bfs(_r, _c):
    queue = deque([(_r, _c)])
    visited[_r][_c] = True

    cnt = 1
    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if nr <= 0 or nr > N or \
                nc <= 0 or nc > M:
                continue

            if board[nr][nc] == 0:
                continue

            if visited[nr][nc]:
                continue

            queue.append((nr, nc))
            visited[nr][nc] = True

            cnt += 1

    return cnt

ans = 0
for r in range(1, N + 1):
    for c in range(1, M + 1):
        if board[r][c] == 0:
            continue

        if not visited[r][c]:
            res = bfs(r, c)

            if res > ans:
                ans = res

print(ans)
