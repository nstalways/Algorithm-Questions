import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
arr = [tuple(map(int, input().split())) for _ in range(N)]

# 풀이
"""
>> 회의 시작 시간을 기준으로, 오름차순 정렬
>> 회의 종료 시간을 저장하는 pq 생성
>> 가장 빨리 종료되는 회의 시간과 새로 시작하는 회의 시간을 비교하였을 때,
>> 크거나 같다면 pop, 작다면 회의실을 추가
>> 새로 시작하는 회의의 종료 시간을 pq에 추가
>> 위 과정을 반복

** 회의실이 추가되면 pq에 저장되는 종료 시간도 누적됨 (pq는 여러 회의실에서 진행되고 있는 회의의 종료 시간이 저장된 곳)
** pq는 min heap을 이용해 구현함으로써, 가장 빨리 끝나는 회의와 새로 시작하는 회의를 비교할 수 있도록 함.
"""
import heapq

arr.sort()

tmp = [0]
cnt = 1
for start, end in arr:
    if start >= tmp[0]:
        heapq.heappop(tmp)
    else:
        cnt += 1

    heapq.heappush(tmp, end)

print(cnt)
