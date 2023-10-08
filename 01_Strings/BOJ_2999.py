import sys

# 전치 행렬
def solution(msg):
    n = len(msg)

    r, c = 0, 0
    for denom in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, denom)
        if mod == 0:
            r, c = denom, div

    if r == 1:
        print(msg)
        return

    mat = [['' for _ in range(c)] for _ in range(r)]
    idx = -1
    for col_idx in range(c - 1 , -1, -1):
        for row_idx in range(r - 1, -1, -1):
            mat[row_idx][col_idx] = msg[idx]
            idx -= 1
    
    res = []
    for row in mat:
        res.append(''.join(row))
    
    print(*res, sep='')


if __name__ == "__main__":
    msg = sys.stdin.readline().strip()
    solution(msg)
