import sys


def solution(num_card, cost_list):
    dp = [0] + cost_list

    for i in range(1, num_card + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] + cost_list[j])

    print(dp[num_card])


if __name__ == "__main__":
    # 입력
    N = int(input())
    P = [0] + list(map(int, sys.stdin.readline().strip().split()))

    solution(N, P)