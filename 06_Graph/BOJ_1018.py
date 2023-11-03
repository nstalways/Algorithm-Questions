import sys
from collections import deque
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

# 풀이
"""
왼쪽 위 상태를 기준으로 8x8을 탐색하고, 결과를 갱신한다.
왼쪽 위 체스의 원래 색깔과 반전한 색깔의 경우 또한 고려해야 한다.
"""
def bfs(r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    res = [float('inf')]

    for color in ['B', 'W']:
        visited = [[False] * M for _ in range(N)]

        queue = deque([(r, c, color)]) # 좌표 + 색깔
        visited[r][c] = True

        cnt = 0
        if color != board[r][c]:
            cnt += 1
        
        append_flag = True
        while queue:
            if cnt >= res[-1]:
                append_flag = False
                break

            cur_r, cur_c, cur_color = queue.popleft()

            for i in range(4):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]

                if nr < r or nr >= r + 8 or \
                    nc < c or nc >= c + 8:
                    continue

                if visited[nr][nc]:
                    continue
                
                next_color = board[nr][nc]
                if cur_color == next_color:
                    next_color = 'B' if cur_color == 'W' else 'W'
                    cnt += 1
                
                queue.append((nr, nc, next_color))
                visited[nr][nc] = True
        
        if append_flag:
            res.append(cnt)

    return min(res)

ans = float("inf")
for r in range(N - 8 + 1):
    for c in range(M - 8 + 1):
        res = bfs(r, c)
        ans = min(ans, res)

print(ans)
