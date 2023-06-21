import sys


def solution(n, p_list):
    p_list = sorted(p_list)

    answer, waiting_time = 0, 0
    for p in p_list:
        waiting_time += p
        answer += waiting_time

    print(answer)


if __name__ == "__main__":
    N = int(input()) # 1 <= N <= 1000
    P_list = list(map(int, sys.stdin.readline().strip().split()))

    solution(N, P_list)
    