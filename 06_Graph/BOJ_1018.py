import sys
from typing import List
from pprint import pprint
from collections import deque
from copy import deepcopy

def solution(board: List[list], start: tuple = (0, 0), limit: tuple = (8, 8)):
    visited = [start]
    queue = deque([start])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= limit[0] or ny < 0 or ny >= limit[1]:
                continue
            
            if (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.append((nx, ny))
                
                if board[x][y] == board[nx][ny]:
                    if board[x][y] == "B":
                        board[nx][ny] = "W"
                    else:
                        board[nx][ny] = "B"
                    
                    answer += 1

    return answer


if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    chess_board = []

    for _ in range(N):
        chess_board.append(list(sys.stdin.readline().strip()))
    
    # 8 x 8 크기로 자르기
    answer = float('inf')
    row_limit, col_limit = 8, 8
    
    for col_start in range(M - col_limit + 1):
        for row_start in range(N - row_limit + 1):
            chess_board_8x8 = []

            for i in range(row_limit):
                chess_board_8x8.append(chess_board[row_start + i][col_start:col_start + col_limit])
            
            for start in [(0, 0), (0, 7), (7, 0), (7, 7)]:
                chess_board_8x8_cp = deepcopy(chess_board_8x8)
                answer = min(answer, solution(chess_board_8x8_cp, start))
    
    print(answer)
    