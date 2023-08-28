import sys

def solution(n, k):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 1

    for i in range(1, k + 1):
        for j in range(n + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % (10**9)
    
    print(dp[-1][-1])


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())

    solution(N, K)
    