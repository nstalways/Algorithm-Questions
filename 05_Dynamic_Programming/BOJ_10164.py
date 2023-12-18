# 입력
N, M, K = map(int, input().split())

# 풀이
"""
DFS -> Python3 부분성공, PyPy3 성공
- 1번부터 동그라미 번호까지 가는 경우의 수 * 동그라미 번호부터 NxM 번호까지 가는 경우의 수
- 동그라미가 없다면, 1번부터 NxM 번호까지 가는 경우의 수 계산

BFS + DP -> Python3 성공
- DFS의 경우 목표 번호까지 갈 수 있는 모든 경로를 하나하나씩 세었음.
- BFS + DP 풀이의 경우 목표 번호까지 가는 경로들을 경우의 수로 기록하여, 불필요한 탐색을 줄임
"""
from collections import deque

arr = [[] for _ in range(N)]
n = 1
mark = (0, 0)
for r in range(N):
    for c in range(M):
        arr[r].append(n)
        if n == K:
            mark = (r, c)

        n += 1

def solution1():
    def dfs(start, end):
        er, ec = end

        cnt = 0
        dr = [1, 0]
        dc = [0, 1]

        stack = [start]

        while stack:
            r, c = stack.pop()

            if (r, c) == end:
                cnt += 1
                continue

            for i in range(2):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr > er or nc > ec:
                    continue

                stack.append((nr, nc))

        return cnt
    
    if not K:
        print(dfs((0, 0), (N-1, M-1)))
    else:
        print(dfs((0, 0), mark) * dfs(mark, (N-1, M-1)))

def solution2():
    def bfs(start, end):
        sr, sc = start
        er, ec = end

        dr = [1, 0]
        dc = [0, 1]

        dp = [[0] * M for _ in range(N)]

        queue = deque([start])
        dp[sr][sc] = 1

        while queue:
            r, c = queue.popleft()

            for i in range(2):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr > er or nc > ec:
                    continue
                
                if dp[nr][nc]:
                    dp[nr][nc] += dp[r][c]
                else:
                    dp[nr][nc] = dp[r][c]
                    queue.append((nr, nc))

        return dp[er][ec]

    if not K:
        print(bfs((0, 0), (N-1, M-1)))
    else:
        print(bfs((0, 0), mark) * bfs(mark, (N-1, M-1)))


if __name__ == "__main__":
    import time

    start = time.time()
    solution1()
    print(f'execution time of solution1: {time.time() - start}')

    start = time.time()
    solution2()
    print(f'execution time of solution2: {time.time() - start}')