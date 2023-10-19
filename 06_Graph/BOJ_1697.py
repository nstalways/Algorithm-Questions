import sys
from collections import deque

def solution(n, k):
    ans = float('inf')
    visited = [False] * (100000 + 1)

    dx = [-1, 1, 2]
    def bfs():
        nonlocal ans

        queue = deque([(n, 0)])
        visited[n] = True

        while queue:
            pos, t = queue.popleft()

            if pos == k:
                ans = min(ans, t)
                break

            for i in range(3):
                if i == 2:
                    n_pos = pos * dx[i]
                else:
                    n_pos = pos + dx[i]

                if n_pos < 0 or n_pos >= 100000 + 1:
                    continue
                
                if not visited[n_pos]:
                    visited[n_pos] = True
                    queue.append((n_pos, t + 1))
        
        print(ans)

    bfs()


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())

    solution(N, K)
