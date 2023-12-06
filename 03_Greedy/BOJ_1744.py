# 풀이
"""
[조건]
- 수열의 두 수를 묶을 수 있다.
- 묶인 숫자들은 서로 곱한다.

[목표]
- 수열의 수들을 적절히 묶어서, 수열의 합이 최대일 때 결과를 출력한다.

[전략 1] heap
- 수열의 합을 최대로 만드려면, (양수, 양수) 혹은 (음수, 음수)의 묶음을 최대한 많이 만들면 된다.
- 단, 두 수의 합이 두 수의 곱보다 큰 경우가 있을 수 있기에 비교 연산이 필요하다.

- 0 이하의 정수 (arr1)와 양수 (arr2)를 서로 다른 리스트에 저장한다.
- 리스트 1을 min heap으로 만들고, 최소 숫자를 가져와 임시 리스트 (tmp)에 저장한다.
    - tmp의 길이가 2일 때, 요소들의 합과 곱을 비교하여 더 큰 결과를 최종 정답에 누적한 뒤 tmp는 초기화한다.
    - 리스트 1이 비었는데 tmp가 남아있다면, 남은 값을 최종 정답에 누적한다.
- 리스트 2를 max heap으로 만들고, 최대 숫자를 가져와 임시 리스트 (tmp)에 저장한다.
    - 리스트 1과 동일하게 수행한다.
"""
import heapq
import math

# 입력
N = int(input())
arr1, arr2 = [], []
for _ in range(N):
    e = int(input())
    if e <= 0:
        arr1.append(e)
    else:
        arr2.append(-e)


def solution(arr, mode='min'):
    res = 0
    tmp = []
    heapq.heapify(arr)

    while arr:
        e = heapq.heappop(arr)

        if mode == 'min':
            tmp.append(e)
        elif mode == 'max':
            tmp.append(-e)

        if len(tmp) == 2:
            res += max(sum(tmp), math.prod(tmp))
            tmp = []

    if tmp:
        res += tmp[0]

    return res

print(solution(arr1, mode='min') + solution(arr2, mode='max'))
