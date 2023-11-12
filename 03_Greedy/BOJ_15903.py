import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
status_lst = list(map(int, input().split()))

# 풀이
"""
min heap을 사용해보자.
"""
import heapq

heapq.heapify(status_lst)
for _ in range(m):
    tmp = 0
    for _ in range(2):
        tmp += heapq.heappop(status_lst)
    
    for _ in range(2):
        heapq.heappush(status_lst, tmp)

print(sum(status_lst))
