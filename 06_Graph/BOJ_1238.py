import sys
import heapq

def dijkstra(graph, start, end):
    time = {village: float('inf') for village in range(1, len(graph))}
    time[start] = 0

    q = [(0, start)] # (누적 시간, 마을 위치)
    while q:
        t, village = heapq.heappop(q)
        if village == end:
            return time[end]

        for next_t, next_village in graph[village]:
            total_t = t + next_t
            if total_t < time[next_village]:
                time[next_village] = total_t
                heapq.heappush(q, (total_t, next_village))


if __name__ == "__main__":
    # 입력
    input = sys.stdin.readline

    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end, t = map(int, input().split())
        graph[start].append((t, end))
    
    # 탐색
    ans = -1
    for village in range(1, N + 1):
        total_time = dijkstra(graph, village, X) + dijkstra(graph, X, village)
        ans = max(ans, total_time)
    
    print(ans)
