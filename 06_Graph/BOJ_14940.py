import sys
from collections import deque
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())

# 풀이
"""
목표 지점부터 bfs 탐색을 수행, 갈 수 있는 땅까지의 거리를 기록
도달할 수 없는 위치는 -1을 출력
>> 도달할 수 없다 -> bfs 탐색이 닿지 않는 곳
>> bfs 탐색이 닿지 않는 곳 -> visited 배열의 값이 False이면서, board의 값이 1인 곳
>> 후처리를 통해 -1을 기록
"""
board = []
start = (0, 0)
for r in range(n):
    tmp = list(map(int, input().split()))
    for c in range(m):
        if tmp[c] == 2:
            start = (r, c)
            tmp[c] = 0

    board.append(tmp)

def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[False] * m for _ in range(n)]

    queue = deque([(*start, 0)]) # 시작 좌표, 거리
    visited[start[0]][start[1]] = True

    while queue:
        r, c, dist = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or \
                nc < 0 or nc >= m:
                continue

            if visited[nr][nc] or board[nr][nc] == 0:
                continue

            queue.append((nr, nc, dist + 1))
            visited[nr][nc] = True

            board[nr][nc] = dist + 1

    # 도달할 수 없는 위치에 대한 후처리
    for r in range(n):
        for c in range(m):
            if board[r][c] == 1 and visited[r][c] == False:
                board[r][c] = -1
    
    for row in board:
        print(*row)

bfs()
