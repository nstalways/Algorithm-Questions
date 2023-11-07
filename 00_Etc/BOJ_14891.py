import sys
from collections import deque
input = sys.stdin.readline

# 입력
status = [deque(list(map(int, list(input().strip())))) for _ in range(4)]
K = int(input().strip())
cmds = [list(map(int, input().split())) for _ in range(K)]

# 풀이
for n, direction in cmds:
    # 톱니바퀴별 회전 방향 탐색
    visited = [False] * 4
    moves = [0] * 4

    visited[n - 1] = True
    moves[n - 1] = direction
    queue = deque([n - 1])

    while queue:
        x = queue.popleft()

        for dx in [-1, 1]:
            nx = x + dx

            if 0 <= nx <= 3 and not visited[nx]:
                if dx == -1 and status[x][6] != status[nx][2]:
                    moves[nx] = -moves[x]
                elif dx == 1 and status[x][2] != status[nx][6]:
                    moves[nx] = -moves[x]
                
                visited[nx] = True
                queue.append(nx)

    # 회전
    for i, move in enumerate(moves):
        status[i].rotate(move)

    
# 점수 계산
score = 0
for i in range(4):
    if status[i][0] == 1:
        score += (2 ** i)

print(score)
