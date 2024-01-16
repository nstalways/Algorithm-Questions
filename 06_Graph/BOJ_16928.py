import sys
from collections import defaultdict
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())

ladders, snakes = defaultdict(int), defaultdict(int)
for i in range(N + M):
    start, end = map(int, input().split())

    if i < N: ladders[start] = end
    else: snakes[start] = end

# 풀이
"""
bfs
- 출발 지점으로부터 1 ~ 6 만큼 이동 && 방문 처리
- 이동한 지점에 사다리 또는 뱀이 있다면, 그에 따라 좌표 업데이트
- 100에 도달한 순간 횟수를 출력
"""
from collections import deque

def solution():
    visited = [False] * (101)

    queue = deque([(1, 0)]) # 현재 좌표, 주사위를 굴린 횟수
    visited[1] = True

    while queue:
        x, cnt = queue.popleft()

        if x == 100:
            print(cnt)
            break

        for dx in range(1, 7):
            nx = x + dx

            if nx <= 100 and not visited[nx]:
                visited[nx] = True

                if ladders[nx]:
                    nx = ladders[nx]
                elif snakes[nx]:
                    nx = snakes[nx]
                
                queue.append((nx, cnt + 1))

solution()
