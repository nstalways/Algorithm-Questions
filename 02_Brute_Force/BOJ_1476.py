import sys


def solution(e, s, m):
    init_e, init_s, init_m = 1, 1, 1
    answer = 1

    while True:
        if (init_e == e) and (init_s == s) and (init_m == m):
            print(answer)
            break

        init_e = (init_e + 1) % 16 + (init_e + 1) // 16
        init_s = (init_s + 1) % 29 + (init_s + 1) // 29
        init_m = (init_m + 1) % 20 + (init_m + 1) // 20

        answer += 1


if __name__ == "__main__":
    E, S, M = list(map(int, sys.stdin.readline().strip().split()))
    
    solution(E, S, M)