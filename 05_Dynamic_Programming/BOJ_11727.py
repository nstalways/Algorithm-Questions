# https://www.acmicpc.net/problem/11727

def solution(n):
    dp = [1, 3] + [0] * (n - 2)

    for idx in range(2, n):
        num_case = dp[idx - 1] + dp[idx - 2] * 2
        dp[idx] = num_case
    
    print(dp[n - 1] % 10007)


if __name__ == "__main__":
    n = int(input())

    solution(n)
