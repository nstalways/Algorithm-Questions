import sys

def solution(N, board):
    """
    1. 사탕 위치를 바꿔본다. 바꾼 경우, 위치를 기록해둔다.
    2. 바꾼 상태에서, 행 방향 또는 열 방향으로 연속된 사탕의 개수를 찾는다.
    """
    def count(updated_board):
        res = 0

        # 행 방향 탐색
        for candies in updated_board:
            cnt = 1
            prev = candies[0]
            for i in range(1, N):
                if prev == candies[i]:
                    cnt += 1
                else:
                    prev = candies[i]
                    res = max(res, cnt)
                    cnt = 1
            
            res = max(res, cnt)
        
        # 열 방향 탐색
        for candies in zip(*updated_board):
            cnt = 1
            prev = candies[0]
            for i in range(1, N):
                if prev == candies[i]:
                    cnt += 1
                else:
                    prev = candies[i]
                    res = max(res, cnt)
                    cnt = 1
            
            res = max(res, cnt)

        return res

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    ans = []
    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr < 0 or nr >= N or \
                    nc < 0 or nc >= N:
                    continue

                a, b = board[r][c], board[nr][nc]

                if a != b:
                    board[r][c] = b
                    board[nr][nc] = a

                    res = count(board)
                    if res == N:
                        print(res)
                        return
                    else:
                        ans.append(res)

                    board[r][c] = a
                    board[nr][nc] = b

    print(max(ans))

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    board = []
    for _ in range(N):
        board.append(list(input().strip())) # C: red, P: blue, Z: green, Y: yellow

    solution(N, board)
