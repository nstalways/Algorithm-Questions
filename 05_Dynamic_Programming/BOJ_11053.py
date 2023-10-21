import sys

def solution(n, data):
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if data[i] > data[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    
    print(max(dp))


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    data = list(map(int, input().split()))

    solution(N, data)
