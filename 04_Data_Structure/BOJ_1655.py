import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())

# 풀이
"""
두 개의 pq를 생성
중앙값을 기준으로 작으면 왼쪽, 크면 오른쪽 pq에 추가
왼쪽 pq는 max heap을, 오른쪽 pq는 min heap을 사용
"""
import heapq

left, right = [], []
n_left, n_right = 0, 0

ans = []
center = None

for i in range(1, N + 1):
    data = int(input().strip())
    if center is None:
        center = data    
        ans.append(center)
        continue

    if data >= center:
        heapq.heappush(right, data)
        n_right += 1
    else:
        heapq.heappush(left, (-data, data))
        n_left += 1

    if (i % 2) == 1 and n_right > n_left:
        heapq.heappush(left, (-center, center))
        n_left += 1

        center = heapq.heappop(right)
        n_right -= 1
    
    elif n_right < n_left:
        heapq.heappush(right, center)
        n_right += 1

        center = heapq.heappop(left)[-1]
        n_left -= 1

    ans.append(center)

print(*ans, sep='\n')
