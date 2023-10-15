# R x C arr, 1 x 1 grid
# (r, c) 위치의 미세먼지 양을 관측
# 공기청정기의 위치: 1열, 크기: 2행
# 공기청정기가 없는 곳에 미세먼지가 존재. A_rc == (r, c)에 있는 미세먼지의 양
# 1초동안 발생하는 일
# 미세먼지 확산. 미세먼지가 있는 모든 칸에서 동시에 발생
# 확산은 인접한 네 방향으로 진행
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로 확산 X
# 확산되는 야은 A_rc / 5, 소수점은 버림
# (r, c)에 남은 미세먼지 양은 A_rc - (A_rc / 5) * (확산된 방향의 개수)
# 공기청정기 작동 -> 공기청정기 위치 기준 위쪽은 반시계방향, 아래쪽은 시계방향 순환
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
# 미세먼지가 공기청정기로 들어가면 모두 정화됨

import sys
from collections import deque
from copy import deepcopy

class MonitoringSystem:
    def __init__(self, r, c, t, arr, pos):
        self.n_rows = r
        self.n_cols = c
        self.times = t
        
        self.room_status = arr

        counter_cw, cw = pos
        self.upper = [(counter_cw, c) for c in range(1, self.n_cols)] + \
                        [(r, self.n_cols - 1) for r in range(counter_cw - 1, -1, -1)] + \
                        [(0, c) for c in range(self.n_cols - 2, -1, -1)] + \
                        [(r, 0) for r in range(1, counter_cw)]
        
        self.lower = [(cw, c) for c in range(1, self.n_cols)] + \
                        [(r, self.n_cols - 1) for r in range(cw + 1, self.n_rows)] + \
                        [(self.n_rows - 1, c) for c in range(self.n_cols - 2, -1, -1)] + \
                        [(r, 0) for r in range(self.n_rows - 2, cw, -1)]
        
        self.counter_cw, self.cw = counter_cw, cw

    def diffusion(self):
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        room_status_tmp = [[0] * self.n_cols for _ in range(self.n_rows)]
        room_status_tmp[self.counter_cw][0] = -1
        room_status_tmp[self.cw][0] = -1

        for r in range(self.n_rows):
            for c in range(self.n_cols):
                state = self.room_status[r][c]

                if state == 0 or state == -1:
                    continue
                
                cnt = 0
                diff_amount = int(state / 5)
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    # 칸이 없을 때
                    if nr < 0 or nr >= self.n_rows or \
                        nc < 0 or nc >= self.n_cols:
                        continue
                    
                    # 공기청정기가 있을 때
                    if self.room_status[nr][nc] == -1:
                        continue
                    
                    # 확산
                    room_status_tmp[nr][nc] += diff_amount
                    cnt += 1
                
                # 업데이트
                room_status_tmp[r][c] += state - (diff_amount * cnt)

        # 최종 업데이트
        self.room_status = room_status_tmp

    def air_cleaning(self):
        prev = 0
        for r, c in self.upper:
            tmp = self.room_status[r][c]

            self.room_status[r][c] = prev
            prev = tmp
        
        prev = 0
        for r, c in self.lower:
            tmp = self.room_status[r][c]

            self.room_status[r][c] = prev
            prev = tmp

    def get_amount_of_dust(self):
        res = 2
        for row in self.room_status:
            res += sum(row)

        return res
    
    def monitoring(self):
        for _ in range(self.times):
            self.diffusion()
            self.air_cleaning()

        res = self.get_amount_of_dust()
        print(res)


if __name__ == "__main__":
    input = sys.stdin.readline

    R, C, T = map(int, input().split())
    arr = []
    pos = []
    for r in range(R):
        tmp = list(map(int, input().split()))
        arr.append(tmp)

        if tmp[0] == -1:
            pos.append(r)

    mss = MonitoringSystem(R, C, T, arr, pos)
    mss.monitoring()
