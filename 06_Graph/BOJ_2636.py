import sys
input = sys.stdin.readline

# 입력
H, W = map(int, input().split())
arr = []
for _ in range(H):
    arr.append(list(map(int, input().split())))

# 풀이
"""
'외부 공기'라면, 해당 위치부터 상/하/좌/우 탐색을 진행하며 닿는 치즈를 저장
>> '외부'와 '내부'는, 공기의 위치에서 상/하/좌/우로 끝까지 갔을 때 가장자리에 닿느냐/닿지 않느냐로 구분할 수 있음

* 더 효율적으로 푸는 방법
>> 가장자리를 논외로 두는 것이 아니라, '가장자리에서' 탐색을 진행하면 외부/내부 공기를 구분할 필요 없음.
>> 가장자리에는 '치즈가 없기' 때문에, 가장자리부터 탐색했을 때 맞닿는 치즈들은 무조건 외부 공기와 맞닿는 치즈들임
>> 따라서 diffuse() 함수를 사용하지 않고도 해결이 가능
"""
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def diffuse(_r, _c):
    flags = []
    for i in range(4):
        factor = 1
        while True:
            nr = _r + dr[i] * factor
            nc = _c + dc[i] * factor

            if nr < 1 or nr >= H - 1 or \
                nc < 1 or nc >= W - 1:
                flags.append(True)
                break

            if arr[nr][nc] == 1:
                flags.append(False)
                break

            factor += 1

    return any(flags)
    

def bfs(_r, _c):
    queue = deque([(_r, _c)])
    visited[_r][_c] = True

    res = []
    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if nr < 1 or nr >= H - 1 or \
                nc < 1 or nc >= W - 1:
                continue

            if visited[nr][nc]:
                continue

            if arr[nr][nc] == 1:
                res.append((nr, nc))
            else:
                queue.append((nr, nc))

            visited[nr][nc] = True

    return res


hour = 0
while True:
    visited = [[False] * W for _ in range(H)]
    n_cheese = 0
    
    target = []
    for r in range(H):
        for c in range(W):
            if arr[r][c] == 1:
                n_cheese += 1

            if not visited[r][c] and arr[r][c] == 0:
                is_outside = diffuse(r, c)

                if is_outside:
                    target.extend(bfs(r, c))

    cnt = len(target)
    if n_cheese - cnt == 0:
        print(hour + 1)
        print(cnt)
        break

    else:
        for r, c in target:
            arr[r][c] = 0

    hour += 1
