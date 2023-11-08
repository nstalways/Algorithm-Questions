import sys
input = sys.stdin.readline

# 입력
N, K = map(int, input().split())
wandv = [0] + [list(map(int, input().split())) for _ in range(N)]

# 풀이
def solution1():
    dp_bags = [[False] * (N + 1) for _ in range(K + 1)]
    dp_values = [0] * (K + 1)

    for i in range(1, K + 1):
        for j in range(1, N + 1):
            w, v = wandv[j]
            if w > i:
                continue

            tmp = dp_values[i - w] + v
            if dp_values[i] < tmp and not dp_bags[i - w][j]:
                dp_values[i] = tmp
                
                dp_bags[i] = dp_bags[i - w][:]
                dp_bags[i][j] = True

    print(max(dp_values))

def knapsack():
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            w, v = wandv[i]
            if w > j:
                dp[i][j]= dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

    print(max(dp[-1]))


solution1()
knapsack()