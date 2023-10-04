import sys

def solution(x):
    cnt = 0

    def q1_ans(n):
        n = int(n)
        if n in [3, 6, 9]:
            print(*[cnt, 'YES'], sep='\n')
        else:
            print(*[cnt, 'NO'], sep='\n')
    
    if len(x) == 1:
        q1_ans(x)
        return

    # need to test
    x_sep = list(map(int, x))
    y = str(sum(x_sep))
    cnt += 1

    while len(y) > 1:
        x_sep = list(map(int, y))
        y = str(sum(x_sep))
        cnt += 1

    q1_ans(y)


if __name__ == "__main__":
    X = sys.stdin.readline().strip()
    solution(X)
