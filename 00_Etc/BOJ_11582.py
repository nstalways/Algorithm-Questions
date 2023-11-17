import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
infos = list(map(int, input().split()))
k = int(input().strip())

# 풀이
"""
구현
"""
ans = infos[:]

factor = 2
while True:
    tmp = []
    for i in range(0, N, factor):
        tmp.extend(sorted(ans[i:i + factor]))

    ans = tmp

    if (N // factor) == k:
        print(*ans)
        break

    factor *= 2
    