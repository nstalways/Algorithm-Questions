import sys
input = sys.stdin.readline

# 입력
M, N = map(int, input().split())
arr = list(map(int, input().split()))

# 풀이
"""
M명의 조카에게 동일한 길이의 과자를 나눠주는데, 이 때 나누어줄 수 있는 과자의 최대 길이를 구해야 함.

조건
    - 조카의 수, 과자의 수: 1 이상 100만 이하
    - 과자의 길이: 1 이상 10억 이하
    - 과자를 하나로 합칠 수 없다. -> DP로 푸는 문제 X

풀이
    - 범위가 큰 편이기 때문에, 이분 탐색으로 접근해볼 법 하다.
"""
lb, ub = 1, max(arr) + 1

ans = 0
while lb <= ub:
    center = (lb + ub) // 2
    
    cnt = 0
    for e in arr:
        cnt += (e // center)

    if cnt < M:
        ub = center - 1
    else:
        lb = center + 1
        if center > ans:
            ans = center

print(ans)
