# 입력
N = int(input())

# 풀이
"""
[조건]
- N: 1 이상 100만 이하의 자연수
- 타일은 00 혹은 1만 존재

[목표]
- N이 주어졌을 때 만들 수 있는 이진수의 가짓수를 세고, 이를 15746으로 나눈 나머지를 출력

[풀이] DP - 피보나치
- N = 6까지 확인했을 때, 피보나치 수열 패턴이 등장
- 목표는 dp[N]을 15746으로 나눈 나머지를 출력하는 것
- dp[N] % 15746 = (dp[N - 1] + dp[N - 2]) % 15746 = dp[N - 1] % 15746 + dp[N - 2] % 15746
- 따라서 dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
"""
dp = [0] * (10**6 + 1)
dp[1], dp[2] = 1, 2
for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N])