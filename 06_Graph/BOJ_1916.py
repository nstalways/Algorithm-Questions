import heapq
import sys


def solution(n, graph, pos):
    start, end = pos

    # 도시 간의 거리 정보 초기화
    costs = {city_num: float('inf') for city_num in range(1, n + 1)}
    costs[start] = 0 # 시작 지점을 0으로 초기화

    queue = [(0, start)] # (거리, 도시 번호)

    while queue:
        curr_cost, curr_city = heapq.heappop(queue)

        # 대상 도시로 이동하기 위한 비용이 이미 저장되어있는 비용보다 크다면 무시
        if curr_cost > costs[curr_city]:
            continue

        if not graph[curr_city]:
            continue
        
        # 인접한 도시를 탐색
        for next_city, transport_cost in graph[curr_city].items():
            next_cost = curr_cost + transport_cost # 인접 도시로 이동하기 위한 비용을 계산

            # 기존 비용보다 더 싸다면
            if next_cost < costs[next_city]:
                costs[next_city] = next_cost # 정보를 업데이트하고
                heapq.heappush(queue, (next_cost, next_city)) # 큐에 추가
    
    print(costs[end])


if __name__ == "__main__":
    num_city = int(input()) # N
    num_bus = int(input()) # M

    bus_info_dict = {city_num: {} for city_num in range(1, num_city+1)}
    for _ in range(num_bus):
        start, end, cost = map(int, sys.stdin.readline().split()) # 시작점, 도착점, 이동 비용
        
        if end in bus_info_dict[start].keys():
            bus_info_dict[start][end] = min(cost, bus_info_dict[start][end])
            continue
            
        bus_info_dict[start][end] = cost

    start_point, end_point = map(int, input().split())

    solution(num_city, bus_info_dict, (start_point, end_point))
