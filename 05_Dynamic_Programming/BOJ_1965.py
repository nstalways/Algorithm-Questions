import sys
input = sys.stdin.readline

# 입력
n = int(input().strip())
size_lst = list(map(int, input().split()))

# 풀이
dp = [1] * n

for i in range(n - 1):
    front = size_lst[i]
    for j in range(i + 1, n):
        if front < size_lst[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
