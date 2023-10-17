import sys
from pprint import pprint
import time

def solution(n_rows, n_cols, paper):
    visited = [[False] * n_cols for _ in range(n_rows)]
    ans = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(r, c, cum_sum, cnt):
        if cnt == 4:
            nonlocal ans
            ans = max(ans, cum_sum)
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n_rows or \
                nc < 0 or nc >= n_cols:
                continue

            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            dfs(nr, nc, cum_sum + paper[nr][nc], cnt + 1)
            visited[nr][nc] = False

    def edge_case(r, c):
        nonlocal ans
        offset_per_direction = {0: [(0, -1), (0, 1), (1, 0)],
                                1: [(-1, 0), (1, 0), (0, -1)],
                                2: [(-1, 0), (0, -1), (0, 1)],
                                3: [(-1, 0), (1, 0), (0, 1)]}
        
        for direction in range(4):
            offset = offset_per_direction[direction]
            cum_sum = paper[r][c]
            for i in range(3):
                dr, dc = offset[i]

                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= n_rows or \
                    nc < 0 or nc >= n_cols:
                    break

                cum_sum += paper[nr][nc]
            
            ans = max(ans, cum_sum)

    for r in range(n_rows):
        for c in range(n_cols):
            visited[r][c] = True
            dfs(r, c, paper[r][c], cnt=1)
            visited[r][c] = False

            edge_case(r, c)

    print(ans)


def solution2(n_rows, n_cols, paper):
    visited = [[False] * n_cols for _ in range(n_rows)]
    max_val = max(map(max, paper))

    ans = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(r, c, cum_sum, cnt):
        nonlocal ans

        # BOJ 기준 이 조건 하나만 없어도 solution2는 시간초과가 발생함
        if cum_sum + max_val * (4 - cnt) <= ans:
            return

        if cnt == 4:
            ans = max(ans, cum_sum)
            return
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n_rows or \
                nc < 0 or nc >= n_cols:
                continue

            if visited[nr][nc]:
                continue

            if cnt == 2:
                visited[nr][nc] = True
                dfs(r, c, cum_sum + paper[nr][nc], cnt + 1)
                visited[nr][nc] = False

            visited[nr][nc] = True
            dfs(nr, nc, cum_sum + paper[nr][nc], cnt + 1)
            visited[nr][nc] = False

    for r in range(n_rows):
        for c in range(n_cols):
            visited[r][c] = True
            dfs(r, c, paper[r][c], cnt=1)
            visited[r][c] = False

    print(ans)


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    paper = []
    for _ in range(N):
        paper.append(list(map(int, input().split())))

    start = time.time()
    solution(N, M, paper)
    print(f'Execution time of solution 1: {time.time() - start:.4f}')
    print('-' * 20)

    start = time.time()
    solution2(N, M, paper)
    print(f'Execution time of solution 2: {time.time() - start:.4f}')
