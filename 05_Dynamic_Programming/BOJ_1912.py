import sys

def solution(n, data):
    dp = data[:]
    for i in range(1, n):
        dp[i] = max(data[i], dp[i - 1] + data[i])

    print(max(dp))
    

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input().strip())
    data = list(map(int, input().split()))

    solution(n, data)
