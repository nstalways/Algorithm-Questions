import sys
from collections import deque
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

# 풀이
def bfs(n):
    visited = [False] * (N + 1)
    memory = [0] + [float('inf')] * N

    queue = deque([(n, 0)])
    visited[n] = True

    while queue:
        cur_n, depth = queue.popleft()
        memory[cur_n] = min(memory[cur_n], depth)

        for next_n in graph[cur_n]:
            if not visited[next_n]:
                queue.append((next_n, depth + 1))
                visited[next_n] = True

    return sum(memory)

ans = (101, float('inf')) # (번호, 케빈 베이컨 수)
for n in range(1, N + 1):
    res = bfs(n)
    if res < ans[-1]:
        ans = (n, res)

print(ans[0])
