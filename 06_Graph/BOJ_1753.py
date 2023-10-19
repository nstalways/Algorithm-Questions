import sys
import heapq

def solution(n_vertex, start, graph):
    """다익스트라 알고리즘 개념만 알면 푸는 문제
    """
    dist = [float('inf')] * (n_vertex + 1)
    dist[start] = 0

    pq = [(0, start)]
    while pq:
        w, v = heapq.heappop(pq)

        if w > dist[v]:
            continue

        for next_v, next_w in graph[v]:
            new_w = w + next_w

            if new_w < dist[next_v]:
                dist[next_v] = new_w
                heapq.heappush(pq, (new_w, next_v))

    for i in range(1, n_vertex + 1):
        res = dist[i]

        if res == float('inf'):
            print('INF')
        else:
            print(res)


if __name__ == "__main__":
    input = sys.stdin.readline

    V, E = map(int, input().split())
    K = int(input().strip())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    
    solution(V, K, graph)
