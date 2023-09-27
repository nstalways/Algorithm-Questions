import sys
from collections import deque

def solution(graph, start, end):
    visited = [False] * len(graph)
    visited[start] = True
    queue = deque([(start, 0)]) # (num_node, dist)

    while queue:
        node, dist = queue.popleft()

        if node == end:
            return dist

        for next_node, next_dist in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, dist + next_dist))


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        node1, node2, dist = map(int, input().split())

        tree[node1].append((node2, dist))
        tree[node2].append((node1, dist))

    ans_per_case = []
    for _ in range(M):
        tg1, tg2 = map(int, input().split())
        res = solution(tree, tg1, tg2)

        ans_per_case.append(res)

    for ans in ans_per_case:
        print(ans)
