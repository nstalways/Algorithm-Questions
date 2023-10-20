def solution(n):
    """
    n == 1 >> 1
    n == 2 >> 2
    n == 3 >> 3
    n == 4 >> 5
    n == 5 >> 8
    ...
    """
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        tmp = dp[i - 1] + dp[i - 2]
        dp.append(tmp)

    print(dp[n] % 10007)


if __name__ == "__main__":
    n = int(input())

    solution(n)
