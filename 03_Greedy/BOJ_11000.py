import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
arr = [tuple(map(int, input().split())) for _ in range(N)]

# 풀이
"""
min heap을 이용한 풀이
>> 회의의 시작 시간을 기준으로 arr를 오름차순 정렬한다.
>> 종료 시간을 기준으로 오름차순 정렬을 진행하는 경우 최소 강의실을 구할 수 없다.
>> 예시: [(1, 5), (2, 4), (3, 6), (5, 7), (4, 8)]
>> 종료 시간을 기준으로 오름차순 정렬을 한다면, (5, 7)이 (2, 4)의 뒤에 가기 때문에 (4, 8)을 위한 추가 회의실 배정이 발생한다.
>> min heap에 저장되는 값은, 이전에 진행 중인 회의의 종료 시각이다.
>> 여러 개의 회의가 진행 중이라고 한다면, 그 중 가장 빨리 종료되는 회의의 시간과 새로운 회의의 시작 시간을 비교한다.
>> 겹치지 않는다면, 해당 회의를 종료(pop)시키고 새로운 회의의 종료 시간을 추가(push)한다.
>> 겹친다면, 회의실을 추가한 뒤 종료 시간을 추가한다.
"""
import heapq

arr.sort()

rooms = [0]
cnt = 1
for start, end in arr:
    if start >= rooms[0]:
        heapq.heappop(rooms)
    else:
        cnt += 1
    
    heapq.heappush(rooms, end)

print(cnt)
