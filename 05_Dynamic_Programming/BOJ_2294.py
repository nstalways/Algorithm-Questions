# 입력
n, k = map(int, input().split())
values = list(set(int(input()) for _ in range(n)))
values.sort()

# 풀이
"""
goal: k를 만들기 위해 필요한 동전의 최소 개수 구하기 (불가능한 경우 -1을 출력)
note:
    - '가치가 같은 동전'이 여러 번 주어질 수 있음 -> 예외처리 필요
    - 각각의 동전은 '몇 개라도 사용할 수 있음'
how:
    - DP
    - 예제 1처럼 15원을 1원, 5원, 12원으로 만들고 싶은 경우,
        14원 + 1원, 10원 + 5원, 3원 + 12원의 비교군이 존재
    - dp[k] = min(dp[k - 1], dp[k - 5], dp[k - 12]) + 1
    - 불가능한 경우 -> 경우의 수가 존재하지 않는 경우
"""
# 보유하고 있는 동전을 기록
dp = [0] * (k + 1)
for value in values:
    try: dp[value] = 1
    except: pass

for i in range(values[0], k + 1):
    tmp = []
    for value in values:
        # 범위 안이면서 경우의 수가 존재하는 경우만 고려
        if 0 <= i - value < k + 1 and dp[i - value]:
            tmp.append(dp[i - value])

    if tmp:
        if dp[i]: dp[i] = min(min(tmp) + 1, dp[i])
        else: dp[i] = min(tmp) + 1

if dp[k]: print(dp[k])
else: print(-1)
