import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
home_lst, store_lst = [], []
for r in range(N):
    arr = list(map(int, input().split()))
    for c in range(N):
        if arr[c] == 1:
            home_lst.append((r, c))
        elif arr[c] == 2:
            store_lst.append((r, c))

# 풀이
def solution_using_loop():
    """단순 반복문을 활용한 풀이
    """
    def get_chicken_dist(home_r, home_c, opened_store_lst):
        dist = float('inf')
        for store_r, store_c in opened_store_lst:
            dist = min(dist, abs(home_r - store_r) + abs(home_c - store_c))

        return dist

    from itertools import combinations

    # 도시의 치킨 거리가 최소일 때, 살아있는 치킨집의 위치 또는 개수를 구하는 것이 아니므로
    # M개 미만의 치킨집은 고려하지 않아도 됨 (살아있는 치킨집을 모두 확인할 것이므로)
    combs = list(combinations(store_lst, M))

    ans = float('inf')
    for comb in combs:
        city_chicken_dist = 0
        for home_r, home_c in home_lst:
            city_chicken_dist += get_chicken_dist(home_r, home_c, comb)

        ans = min(ans, city_chicken_dist)

    print(ans)

def dfs_with_backtracking():
    """dfs + backtracking을 활용한 풀이
    """
    def get_chicken_dist(opened_store_lst):
        chicken_dist = 0
        for home_r, home_c in home_lst:
            tmp = float('inf')
            for store_r, store_c in opened_store_lst:
                dist = abs(home_r - store_r) + abs(home_c - store_c)
                if tmp > dist:
                    tmp = dist

            chicken_dist += tmp

        return chicken_dist

    city_chicken_dist = float('inf')
    def dfs(depth, idx, stack=[]):
        if depth == M:
            nonlocal city_chicken_dist
            tmp = get_chicken_dist(stack)
            if city_chicken_dist > tmp:
                city_chicken_dist = tmp
            
            return

        for i in range(idx, len(store_lst)):
            stack.append(store_lst[i])
            dfs(depth + 1, i + 1, stack)
            stack.pop()

    dfs(0, 0, stack=[])
    print(city_chicken_dist)

solution_using_loop()
dfs_with_backtracking()