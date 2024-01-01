import sys
input = sys.stdin.readline

# 입력
N, d, k, c = map(int, input().split())
arr = [int(input().strip()) for _ in range(N)]

# 풀이
"""
브루트 포스, 구현, 해쉬 맵, 자료구조, 최적화, 
- 큐 두 개를 이용하여 구현
- 첫 번째 큐는 먹을 접시, 두 번째 큐는 남은 회전 초밥
- 첫 번째 큐에 k개만큼의 접시가 차면, 종류의 가짓수를 확인하여 정답을 갱신 + 이후 첫 번째 큐의 첫 번째 원소를 두 번째 큐의 끝에 추가
- 위 과정을 반복
- 대략적인 시간 복잡도: O(N)
"""
from collections import deque

params = {
    'stop_condition': 0,
    'sushi_table': [0] * (d + 1),
    'n_dish': 0,
}

queue = deque()
arr = deque(arr)

answer = 0

while params['stop_condition'] < N:
    cur_dish = arr.popleft()
    queue.append(cur_dish)

    params['sushi_table'][cur_dish] += 1
    params['n_dish'] += 1

    if params['n_dish'] == k:
        n_kinds = len(set(queue))
        if not params['sushi_table'][c]:
            n_kinds += 1

        if n_kinds > answer:
            answer = n_kinds

        tmp = queue.popleft()

        params['sushi_table'][tmp] -= 1
        params['n_dish'] -= 1

        arr.append(tmp)
        params['stop_condition'] += 1
    
print(answer)
