import sys
from collections import deque

def solution(N, M, r, c, d, room_status):
    # (북, 동, 남, 서)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    cnt = 0
    
    queue = deque([(r, c, d)])
    while queue:
        cur_r, cur_c, cur_d = queue.popleft()

        if room_status[cur_r][cur_c] == 0:
            room_status[cur_r][cur_c] = 2
            cnt += 1

        new_d = cur_d
        go_back = True
        for _ in range(4):
            new_d = (new_d + 3) % 4

            nr = cur_r + dr[new_d]
            nc = cur_c + dc[new_d]

            if nr < 0 or nr >= N or \
                nc < 0 or nc >= M:
                continue

            if room_status[nr][nc] == 0:
                queue.append((nr, nc, new_d))
                go_back = False
                break

        if go_back:
            nr = cur_r - dr[cur_d]
            nc = cur_c - dc[cur_d]

            if 0 < nr < N and 0 < nc < M and room_status[nr][nc] != 1:
                queue.append((nr, nc, cur_d))
    
    print(cnt)


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    
    room_status = []
    for _ in range(N):
        room_status.append(list(map(int, input().split())))

    solution(N, M, r, c, d, room_status)
