import sys
input = sys.stdin.readline

# 풀이
"""
[조건]
- '#': 못 지나감 / '.': 지나감 / 'S': 시작 지점 / 'E': 출구
- 각 칸에서 인접한 6개의 칸 (동, 서, 남, 북, 상, 하)로 1분의 시간을 들여 이동할 수 있음 -> 배열이 3차원임
- 출구를 통해서만 탈출할 수 있음

[전략]
- BFS를 이용한 탐색 + 구현 문제
"""
from collections import deque

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dl = [0, 0, 0, 0, -1, 1]

def bfs():
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    s_l, s_r, s_c = pos_s

    queue = deque([(s_l, s_r, s_c, 0)]) # 시작 좌표 + time
    visited[s_l][s_r][s_c] = True

    while queue:
        cur_l, cur_r, cur_c, cur_t = queue.popleft()

        # 종료 조건
        if building[cur_l][cur_r][cur_c] == 'E':
            return f'Escaped in {cur_t} minute(s).'
        
        for i in range(6):
            nl = cur_l + dl[i]
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            # 현재 층을 벗어나는 경우
            if nl < 0 or nl >= L or \
                nr < 0 or nr >= R or \
                nc < 0 or nc >= C:
                continue
            
            # 지나갈 수 없는 경우
            if building[nl][nr][nc] == '#':
                continue
            
            # 이미 방문한 위치인 경우
            if visited[nl][nr][nc]:
                continue

            queue.append((nl, nr, nc, cur_t + 1))
            visited[nl][nr][nc] = True


    return 'Trapped!'


ans = []
while True:
    L, R, C = map(int, input().split())

    if (L, R, C) == (0, 0, 0):
        print(*ans, sep='\n')
        break

    building = []
    pos_s = (0, 0, 0)

    for l in range(L):
        floor = []
        for r in range(R):
            tmp = list(input().strip())

            try:
                c = tmp.index('S')
                pos_s = (l, r, c)
            except:
                pass
            
            floor.append(tmp)

        building.append(floor)

        input().strip()
    
    ans.append(bfs())
