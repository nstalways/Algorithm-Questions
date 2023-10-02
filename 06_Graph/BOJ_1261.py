import sys
import heapq

def solution(maze, n, m):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    cnts = {room_num: float('inf') for room_num in range(1, n * m + 1)}
    cnts[1] = 0
    pq = [(0, 0, 0)]

    while pq:
        cnt, r, c = heapq.heappop(pq)

        if (r, c) == (n - 1, m - 1):
            print(cnts[n * m])
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            next_cnt = cnt + maze[nr][nc]
            next_room_num = nr * m + (nc + 1)

            if next_cnt < cnts[next_room_num]:
                cnts[next_room_num] = next_cnt
                heapq.heappush(pq, (next_cnt, nr, nc))


if __name__ == "__main__":
    input = sys.stdin.readline

    M, N = map(int, input().split())
    maze = []
    for _ in range(N):
        maze.append([int(x) for x in list(input().strip())])
    
    solution(maze, N, M)
