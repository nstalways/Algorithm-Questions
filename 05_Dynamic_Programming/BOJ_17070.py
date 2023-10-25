import sys

# dfs로 접근 -> 테케는 맞으나, 시간 초과
def solution(N, house):
    cnt = 0

    pipe_state = {(0, 1): 'width',
                  (1, 0): 'length',
                  (1, 1): 'diagonal'}

    moves = {'width': [(0, 1), (1, 1)],
             'length': [(1, 0), (1, 1)],
             'diagonal': [(0, 1), (1, 1), (1, 0)]}

    def dfs(r, c, state):
        nonlocal cnt

        if (r, c) == (N - 1, N - 1):
            cnt += 1
            return
    
        for dr, dc in moves[state]:
            nr = r + dr
            nc = c + dc

            if nr >= N or nc >= N:
                continue
            
            next_state = pipe_state[(dr, dc)]
            if house[nr][nc] == 0:
                if next_state == 'diagonal':
                    # 추가 검증
                    if house[nr - 1][nc] == 0 and house[nr][nc - 1] == 0:
                        dfs(nr, nc, next_state)

                else:
                    dfs(nr, nc, next_state)

    dfs(0, 1, 'width')
    print(cnt)

# 통과
def solution2(N, house):
    # dp[0][r][c]: (r, c) 지점에 가로 파이프의 끝이 오는 경우의 수
    # dp[1][r][c]: (r, c) 지점에 세로 파이프의 끝이 오는 경우의 수
    # dp[2][r][c]: (r, c) 지점에 대각선 파이프의 끝이 오는 경우의 수
    dp = [[[0] * N for _ in range(N)] for _ in range(3)]
    
    for c in range(1, N):
        if house[0][c] == 1:
            break

        dp[0][0][c] = 1
    
    for r in range(1, N):
        for c in range(1, N):
            # 가로, 세로 파이프
            if house[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
                dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

                if house[r - 1][c] == 0 and house[r][c - 1] == 0:
                    dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

    res = dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1]
    print(res)


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    house = []
    for _ in range(N):
        house.append(list(map(int, input().split())))

    solution(N, house)    
    solution2(N, house)
