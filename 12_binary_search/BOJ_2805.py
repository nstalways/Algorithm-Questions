import sys

def solution(N, M, heights):
    lb, ub = 0, max(heights)

    while True:
        if lb > ub:
            print(ub)
            break

        setting = (lb + ub) // 2
        cum_sum = 0
        for height in heights:
            if height >= setting:
                cum_sum += (height - setting)

        if cum_sum < M:
            ub = setting - 1
        else:
            lb = setting + 1


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    heights = list(map(int, input().split()))

    solution(N, M, heights)
