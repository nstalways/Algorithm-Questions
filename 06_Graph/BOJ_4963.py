import sys
from collections import deque

# bfs
def solution(w, h, board):
    visited = [[False] * w for _ in range(h)]
    cnt = 0

    # (상, 하, 좌, 우, 대각선 4개)
    dr = [-1, 1, 0, 0, -1, 1, -1, 1]
    dc = [0, 0, -1, 1, -1, -1, 1, 1]

    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True

        while queue:
            r, c = queue.popleft()

            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr < 0 or nr >= h or \
                    nc < 0 or nc >= w:
                    continue

                if board[nr][nc] == 0:
                    continue
                
                if not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = True
    
    for r in range(h):
        for c in range(w):
            if visited[r][c]:
                continue

            if board[r][c] == 0:
                continue

            bfs(r, c)
            cnt += 1

    return cnt


if __name__ == "__main__":
    input = sys.stdin.readline

    ans = []
    while True:
        w, h = map(int, input().split())

        if (w, h) == (0, 0):
            print(*ans, sep='\n')
            break

        board = []
        for _ in range(h):
            board.append(list(map(int, input().split())))

        res = solution(w, h, board)
        ans.append(res)
