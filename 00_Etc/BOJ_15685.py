import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
arr = [list(map(int ,input().split())) for _ in range(N)]

# 풀이
"""
[구현]
- 끝 점을 기준으로 시계 방향 90도 회전
- 회전 시 이전 세대의 모든 좌표를 회전시켜야 함
- 좌표에 대한 방문 처리가 필요
- 이전 세대의 방향 정보가 필요
"""
# 좌표 방문 처리 배열
crds = [[False] * 101 for _ in range(101)]

# 방향
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def solution(c, r, d, g):
    # 기본 처리
    nr = r + dr[d]
    nc = c + dc[d]

    crds[r][c] = True
    crds[nr][nc] = True

    # 알고리즘
    directions = [d]
    cur_g = 0
    while cur_g < g:
        directions_cp = directions[:]
        
        for direction in directions_cp[::-1]:
            nd = (direction + 1) % 4

            nr = nr + dr[nd]
            nc = nc + dc[nd]

            crds[nr][nc] = True
            directions.append(nd)

        cur_g += 1


for e in arr:
    solution(*e)

cnt = 0
for r in range(100):
    for c in range(100):
        if all([crds[r][c], crds[r][c + 1], crds[r + 1][c], crds[r + 1][c + 1]]):
            cnt += 1

print(cnt)            
