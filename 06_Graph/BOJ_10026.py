from collections import deque
import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
arr = []
for _ in range(N):
    arr.append(list(input().strip()))

# 풀이: BFS
def solution(flag=False):
    def bfs(crds):
        queue = deque([crds])
        visited[crds[0]][crds[1]] = True

        while queue:
            r, c = queue.popleft()

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 그리드를 벗어나는 경우
                if nr < 0 or nr >= N or \
                    nc < 0 or nc >= N:
                    continue

                # 이미 방문한 위치인 경우
                if visited[nr][nc]:
                    continue

                # 적록색약인 경우
                if flag:
                    if arr[r][c] in ['R', 'G'] and arr[nr][nc] == 'B' or \
                        arr[r][c] == 'B' and arr[nr][nc] in ['R', 'G']:
                        continue

                    visited[nr][nc] = True
                    queue.append((nr, nc))

                # 적록색약이 아닌 경우
                else:
                    if arr[r][c] != arr[nr][nc]:
                        continue
                    
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    visited = [[False] * N for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                bfs((r, c))
                cnt += 1

    return cnt

print(solution(flag=False), solution(flag=True))