import sys
from collections import deque

def solution(n, graph, construction_times, target):
    # 정점별 진입 차수 계산
    in_degree = [0] * (n + 1)
    for _, vertex_info in enumerate(graph):
        for next_vertex in vertex_info:
            in_degree[next_vertex] += 1
    
    # 진입 차수가 0인 정점들을 queue에 저장
    # 정점별 기본 시간 초기화
    queue = deque()
    dp = [0] * (n + 1)
    for vertex in range(1, n + 1):
        dp[vertex] = construction_times[vertex]

        if in_degree[vertex] == 0:
            queue.append(vertex)

    # 위상 정렬 + DP
    while queue:
        vertex = queue.popleft()

        # 현재 정점과 연결되어있는 정점을 탐색
        for next_vertex in graph[vertex]:
            # 연결된 정점까지의 소요 시간을 dp에 기록. 여러 경로가 있는 경우, 문제 조건에 따라 최대값을 dp에 저장
            total_time = dp[vertex] + construction_times[next_vertex]
            dp[next_vertex] = max(dp[next_vertex], total_time)

            in_degree[next_vertex] -= 1 # 정점 하나가 사라졌으므로, 진입 차수 감소

            # 진입 차수가 0인 새로운 정점이 발견된 경우, 큐에 추가
            if in_degree[next_vertex] == 0:
                queue.append(next_vertex)

        # 목표 건물의 진입 차수가 0인 경우 종료
        if in_degree[target] == 0:
            break

    return dp[target]
    

if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input().strip())

    ans_per_case = []
    for _ in range(T):
        N, K = map(int, input().split())
        construction_times = [0] + list(map(int, input().split()))

        build = [[] for _ in range(N + 1)]
        
        for _ in range(K):
            X, Y = map(int, input().split())
            build[X].append(Y)

        W = int(input().strip())

        ans_per_case.append(solution(N, build, construction_times, W))

    for ans in ans_per_case:
        print(ans)
        