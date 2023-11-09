import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
order_lst = []
prefer_lst = [[] for _ in range(N**2 + 1)]

for _ in range(N**2):
    tmp = list(map(int, input().split()))

    order_lst.append(tmp[0])
    prefer_lst[tmp[0]].extend(tmp[1:])

# 풀이
"""
1. 주어진 조건에 따라 학생들을 배치
2. 배치가 끝나면, 상/하/좌/우를 탐색하며 점수 계산
"""
from collections import deque

# 학생 배치
classroom = [[0] * N for _ in range(N)]
order_lst_cp = deque(order_lst[:])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

is_first = True
while order_lst_cp:
    cur_student = order_lst_cp.popleft()

    if is_first: # 첫 번째 학생은 무조건 (1, 1)에 배치
        classroom[1][1] = cur_student
        is_first = False
        continue
    
    # 조건에 맞게 새로운 학생을 배치하는 과정
    candidates = []
    for r in range(N):
        for c in range(N):
            if classroom[r][c]:
                continue

            empty_seats = 0
            likes = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr < 0 or nr >= N or \
                    nc < 0 or nc >= N:
                    continue

                if not classroom[nr][nc]:
                    empty_seats += 1
                    continue

                if classroom[nr][nc] in prefer_lst[cur_student]:
                    likes += 1

            candidates.append((likes, empty_seats, r, c))
    
    candidates.sort(reverse=True, key=lambda x: (x[0], x[1], -x[2], -x[3]))
    _, _, seat_r, seat_c = candidates[0]

    classroom[seat_r][seat_c] = cur_student

# 만족도 조사
score = 0
for r in range(N):
    for c in range(N):
        cnt = 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or \
                nc < 0 or nc >= N:
                continue

            if classroom[nr][nc] in prefer_lst[classroom[r][c]]:
                cnt += 1

        if cnt > 0:
            score += (10 ** (cnt - 1))

print(score)
