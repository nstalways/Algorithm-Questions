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
cur_city, next_city = 0, 1
dist = roads[cur_city]
ans = 0

while True:
    if prices[cur_city] < prices[next_city]:
        dist += roads[next_city]

        if next_city == N - 2:
            ans += (prices[cur_city] * dist)
            break
    
    else:
        ans += (prices[cur_city] * dist)

        if next_city == N - 1:
            break

        cur_city = next_city
        dist = roads[cur_city]

    next_city += 1

print(ans)
