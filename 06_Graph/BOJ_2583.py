import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split()) # 100 이하의 자연수

# board 초기화
board = [[0] * N for _ in range(M)]
for _ in range(K):
    lb_x, lb_y, ru_x, ru_y = map(int, input().split())

    # 좌표 맞춰주기
    lb_y = (M - 1) - lb_y
    ru_y = M - ru_y

    for r in range(ru_y, lb_y + 1):
        for c in range(lb_x, ru_x):
            board[r][c] = 1

# TODO: BFS
def bfs(r, c, group):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque([(r, c)])

    area = 1
    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if nr < 0 or nr >= M or \
                nc < 0 or nc >= N:
                continue

            if not board[nr][nc]:
                queue.append((nr, nc))
                board[nr][nc] = group
                area += 1

    return area

cnt, ans = 0, []
group = 2
for r in range(M):
    for c in range(N):
        if not board[r][c]:
            board[r][c] = group
            ans.append(bfs(r, c, group))
            cnt += 1

            group += 1

ans.sort()

print(cnt)
print(*ans)
