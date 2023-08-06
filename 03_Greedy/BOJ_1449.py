import sys


def solution(pos_list, tape_length):
    pos_list = sorted(pos_list)
    pos_list = [2*pos for pos in pos_list]
    pipe = [1 if pos in pos_list else 0 for pos in range(1000*2 + 1)]

    n_tape = 0
    for pos in pos_list:
        if pipe[pos] > 1:
            continue
        
        start = pos - 1
        for idx in range(start, start+(2*tape_length)):
            if idx > len(pipe) - 1:
                break

            pipe[idx] += 1

        n_tape += 1       

    print(n_tape) 


if __name__ == "__main__":
    N, L = map(int, input().split())

    target = list(map(int, sys.stdin.readline().split()))

    solution(target, L)
    