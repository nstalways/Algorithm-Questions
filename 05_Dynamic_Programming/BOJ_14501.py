import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

# 풀이
"""
DP 문제
>> dp 배열의 i번째 값 dp[i]는 i번째 날짜까지 벌 수 있는 최대 수익을 의미함.
>> 오늘 날짜를 i, 상담 기간을 t_i, 수익을 p_i라고 하면, dp[i + t_i] = max(dp[i + t_i], dp[i] + p_i)
"""
dp = [0] * (N + 2)
for day, info in enumerate(arr, start=1):
    t, p = info
    if day + t > N + 1:
        continue
    else:
        dp[day + t] = max(dp[day + t], max(dp[:day + 1]) + p)

print(max(dp))
