import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

# 풀이
"""
DP를 이용한 풀이
- 점화식 세우기
- dp[i] : 현재 i번째 날일 때, 얻을 수 있는 최대 수익
- 현재 i번쨰 날이고, 상담 기간을 t_i, 수익을 p_i라고 하면
- dp[i + t_i]= max(dp[i + t_i - 1], i번째 날짜까지의 최대 수익 + p_i)
"""
dp = [0] * (N + 2)
prev_best = 0

for today, data in enumerate(arr, start=1):
    duration, profit = data
    if dp[today] > prev_best:
        prev_best = dp[today]
        
    if today + duration - 1 > N:
        continue   

    dp[today + duration] = max(dp[today + duration], prev_best + profit)

print(max(dp))
