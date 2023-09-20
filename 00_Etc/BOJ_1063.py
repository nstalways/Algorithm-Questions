import sys

def solution(pos_king, pos_stone, moves):
    # king과 stone의 위치를 숫자로 변환하기
    str2int_dict = {chr(alpha): row_idx for row_idx, alpha in enumerate(range(65, 65 + 8), start=1)}
    int2str_dict = {row_idx: chr(alpha) for row_idx, alpha in enumerate(range(65, 65 + 8), start=1)}

    # move에 따른 좌표 변화량
    how2move_dict = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0),
                     'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}
    
    # (row_idx, col_idx)
    pos_king = (int(pos_king[-1]), str2int_dict[pos_king[0]])
    pos_stone = (int(pos_stone[-1]), str2int_dict[pos_stone[0]])
    
    # 이동
    for move in moves:
        d_row, d_col = how2move_dict[move]
        n_pos_king = (pos_king[0] + d_row, pos_king[1] + d_col)

        # 유효성 검증
        if 1 <= n_pos_king[0] <= 8 and 1 <= n_pos_king[1] <= 8:
            if n_pos_king != pos_stone:
                pos_king = n_pos_king
                continue

            n_pos_stone = (pos_stone[0] + d_row, pos_stone[1] + d_col)

            if 1 <= n_pos_stone[0] <= 8 and 1 <= n_pos_stone[1] <= 8:
                pos_king = n_pos_king
                pos_stone = n_pos_stone
    
    # 이동 완료 후 체스판 좌표로 변환
    pos_king = int2str_dict[pos_king[1]] + str(pos_king[0])
    pos_stone = int2str_dict[pos_stone[1]] + str(pos_stone[0])

    print(pos_king)
    print(pos_stone)


if __name__ == "__main__":
    pos_king, pos_stone, N = sys.stdin.readline().split()

    moves = []
    for _ in range(int(N)):
        moves.append(sys.stdin.readline().strip())

    solution(pos_king, pos_stone, moves)
