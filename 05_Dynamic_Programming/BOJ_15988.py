import sys
import time
input = sys.stdin.readline

# 입력
T = int(input().strip())

# 풀이
start = time.time()
dp = [0] * (10 ** 6 + 1)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 1000000 + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for _ in range(T):
    print(dp[int(input().strip())])
    