# 입력
N, K = map(int, input().split())

# 풀이
"""
goal: 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 "가장 빠른 시간이 몇 초 후"인지 구하기
note:
    - 현재 위치가 X일 때 걷는다면, 1초 후에 X-1 또는 X+1로 이동
    - 순간이동을 하는 경우 0초 후에 2*X의 위치로 이동
how:
    - 다익스트라 탐색
    - 탐색 범위를 합리적으로 제한하면 시간을 더 단축할 수 있음
"""
import heapq

lim = 10**5 + 1
times = [float('inf')] * lim

pq = [(0, N)] # (시간, 현재 위치)
times[N] = 0
while pq:
    t, x = heapq.heappop(pq)
    if x == K:
        print(t)
        break

    # 뒤, 앞
    for move in [-1, 1]:
        nx = x + move

        if 0 <= nx < lim and t + 1 < times[nx]:
            times[nx] = t + 1
            heapq.heappush(pq, (t + 1, nx))

    # 순간이동
    nx = 2*x
    if 0 <= nx < lim and t < times[nx]:
        times[nx] = t
        heapq.heappush(pq, (t, nx))
