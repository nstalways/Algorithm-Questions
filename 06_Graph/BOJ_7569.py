import sys
from collections import deque
input = sys.stdin.readline

# 입력
M, N, H = map(int, input().split()) # col, row, height
arr = []
queue = deque() # 시작 지점을 미리 저장하는 것이 핵심
for k in range(H):
    tmp = []
    for i in range(N):
        tmts = list(map(int, input().split()))
        for j in range(M):
            if tmts[j] == 1:
                queue.append((k, i, j))

        tmp.append(tmts)

    arr.append(tmp)

# 풀이: BFS
def bfs():
    move = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]

    while queue:
        k, i, j = queue.popleft()
        
        for dk, di, dj in move:
            nk = k + dk
            ni = i + di
            nj = j + dj

            # 상자 범위 안이면서 아직 익지 않은 토마토라면
            if 0 <= nk < H and 0 <= ni < N and 0 <= nj < M and \
                arr[nk][ni][nj] == 0:

                arr[nk][ni][nj] = arr[k][i][j] + 1
                queue.append((nk, ni, nj))

    # 탐색을 마친 뒤 토마토 상태를 확인
    day = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                e = arr[k][i][j]
                if e == 0:
                    print(-1)
                    return
    
                if e > day:
                    day = e

    print(day - 1)

bfs()
