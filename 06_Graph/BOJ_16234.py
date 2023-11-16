"""
입력: NxN 크기의 땅
세부 정보: 
    1x1 크기의 땅에는 나라가 하나씩 존재
    땅이 A라고 했을 때, A[r][c]는 해당 나라에 살고 있는 인구의 수
    인접한 나라 사이에는 국경선이 존재
구현 조건:
    인구 이동은 하루 동안 진행하며, 더 이상 인구 이동이 없을 때까지 지속
    1. 국경선을 공유하는 두 나라의 인구 차이가 L이상 R이하라면, 국경선을 open
    2. 모든 나라에 대해 1을 확인한 뒤, 인구 이동을 수행
    3. 국경선이 열려있어 연결된 나라들을 연합이라 부르며, 연합을 이루고 있는 각 칸의 인구수는
        연합의 인구수 / 연합을 이루고 있는 칸의 개수 (소수점은 버림)
    4. 연합 해체
출력:
    인구 이동이 며칠 동안 발생하는지 출력

풀이:
    bfs를 이용한 clustering & 인구 이동 구현
"""
import sys
from collections import deque
input = sys.stdin.readline

# 입력
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 풀이
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True

    memory = [(r, c)]
    num_people = board[r][c]
    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if nr < 0 or nr >= N or \
                nc < 0 or nc >= N:
                continue

            if visited[nr][nc]:
                continue

            diff = abs(board[cur_r][cur_c] - board[nr][nc])
            if diff >= L and diff <= R:
                queue.append((nr, nc))
                visited[nr][nc] = True

                memory.append((nr, nc))
                num_people += board[nr][nc]

    num_country = len(memory)
    after_move = int(num_people / num_country)
    for r, c in memory:
        board[r][c] = after_move

    return True if num_country > 1 else False

day = 0
while True:
    visited = [[False] * N for _ in range(N)]

    is_united = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                flag = bfs(r, c)
                
                if flag == True:
                    is_united = True

    if is_united == False:
        print(day)                
        break

    day += 1
