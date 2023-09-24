import sys

def solution(chessboard):
    cnt = 0

    for row_idx, row in enumerate(chessboard):
        is_first = (row_idx + 1) % 2
        for col_idx, piece in enumerate(row):
            if is_first:
                if (col_idx % 2) == 0 and piece == 'F':
                    cnt += 1

            else:
                if (col_idx % 2) == 1 and piece == 'F':
                    cnt += 1
    
    print(cnt)


if __name__ == "__main__":
    chessboard = []

    for _ in range(8):
        chessboard.append(list(sys.stdin.readline().strip()))

    solution(chessboard)
    