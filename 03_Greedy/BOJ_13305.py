import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

# 풀이
"""
핵심: 가격이 저렴한 주유소에서 최대한 많이 충전한다.
"""
cur_price = prices[0]
ans = 0

for i in range(N - 1):
    if cur_price > prices[i]:
        cur_price = prices[i]
    ans += (cur_price * roads[i])

print(ans)
