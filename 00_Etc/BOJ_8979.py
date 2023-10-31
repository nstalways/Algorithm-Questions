import sys
input = sys.stdin.readline

# 입력
N, K = map(int, input().split())
info_lst = [tuple(map(int, input().split())) for _ in range(N)]

# 풀이
# 1. (금, 은, 동) 갯수대로 정렬
info_lst.sort(reverse=True, key=lambda x: (x[1], x[2], x[3]))

# 2. K 국가의 등수 출력
records = [0] * (N + 1)

prev = []
for order, info in enumerate(info_lst, start=1):
    if prev[1:] == info[1:]:
        records[info[0]] = records[prev[0]]
    else:
        records[info[0]] = order

    prev = info

print(records[K])
