import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())

# 풀이
"""
M개의 치킨집을 고른 뒤 도시의 치킨 거리를 구해서, 최소값을 갱신해나간다 -> 브루트포스
>> BFS로 접근 시 시간 초과가 발생 >> 단순 반복문을 이용할 것
"""
city_infos = []
stores = []
for r in range(N):
    arr = list(map(int, input().split()))
    for c in range(N):
        if arr[c] == 2:
            stores.append((r, c))
    
    city_infos.append(arr)

from itertools import combinations

def get_chicken_dist(r, c, opened_stores):
    dist = float('inf')
    for store_r, store_c in opened_stores:
        dist = min(dist, abs(r - store_r) + abs(c - store_c))

    return dist

ans = float('inf')
for m in range(1, M + 1):
    selected_lst = list(combinations(stores, m))

    for selected in selected_lst:
        city_chicken_dist = 0
        for r in range(N):
            for c in range(N):
                if city_infos[r][c] == 1:
                    city_chicken_dist += get_chicken_dist(r, c, selected)
        
        ans = min(ans, city_chicken_dist)

print(ans)
