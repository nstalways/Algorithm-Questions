# 입력
n = int(input())
infos = [0] + [int(input()) for _ in range(n)]

# 풀이
def solution():
    if n <= 2:
        print(sum(infos))
        return

    dp = [0] * (n + 1)
    dp[1] = infos[1]
    dp[2] = dp[1] + infos[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + infos[i - 1] + infos[i], dp[i - 2] + infos[i], dp[i - 1])
    
    print(max(dp))

solution()
