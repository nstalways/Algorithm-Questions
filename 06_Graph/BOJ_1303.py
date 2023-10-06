import sys
from collections import deque

def solution(place, n_cols, n_rows):
    visited = [[False] * n_cols for _ in range(n_rows)]

    def bfs(start, ignore):
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        queue = deque([start])
        visited[start[0]][start[1]] = 1
        cnt = 1

        while queue:
            r, c = queue.popleft()

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr < 0 or nr >= n_rows or\
                    nc < 0 or nc >= n_cols:
                    continue

                if place[nr][nc] == ignore:
                    continue

                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
                    cnt += 1
        
        return cnt
    
    # TODO: 모든 지점 탐색 로직 작성
    ans = [0, 0]
    for i in range(n_rows):
        for j in range(n_cols):
            if visited[i][j]:
                continue

            if place[i][j] == 'W':
                ans[0] += bfs((i, j), 'B') ** 2
            else:
                ans[1] += bfs((i, j), 'W') ** 2

    print(*ans, sep=' ')


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    place = []
    for _ in range(M):
        place.append(list(input().strip()))

    solution(place, N, M)
