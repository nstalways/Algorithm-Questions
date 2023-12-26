import sys
input = sys.stdin.readline

# 입력
T = int(input().strip())

# 풀이
"""
조합을 이용한 풀이 -> 시간 초과
- 종류별 의상 개수를 센다
- 의상 종류 조합을 찾은 뒤, 종류별 의상 개수를 곱해 경우의 수를 계산한다.

아이디어가 중요
- 종류별 의상 개수를 센다
- 종류별 의상 개수에 1을 더한 값을 모든 종류에 대해 곱한다. 여기서 1은 해당 의상을 착용하지 않는 경우의 수를 의미한다.
- 이전에 계산한 값에서 1을 뺀다.여기서 1은 알몸인 상태를 의미한다. 알몸인 경우를 제외해야하기 때문에, 1을 빼준다.
"""
from collections import defaultdict

ans = []
for _ in range(T):
    closet = defaultdict(int)

    n = int(input().strip())
    for _ in range(n):
        _, cat = input().split()
        closet[cat] += 1

    n_cases = 1
    for _, n_items in closet.items():
        n_cases *= (n_items + 1)

    ans.append(n_cases - 1)

print(*ans, sep='\n')
