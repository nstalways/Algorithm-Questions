import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 풀이
"""
문제 해석
- 크기가 같은 M개의 블루레이로 주어진 강의 모두를 녹화할 수 있어야 한다.
- 이를 가능하게 하는 블루레이의 크기 중 최소를 구해야 한다.

핵심
- M개 이하의, 크기가 모두 같은 블루레이를 이용하여 주어진 강의를 모두 녹화할 수 있어야 한다.

전략: 이진 탐색을 이용한 구현
1 계산한 중앙값을 블루레이의 크기로 이용한다.
2 순서대로 강의를 담으면서 메모리를 체크하고, 메모리가 중앙값보다 크다면 개수를 센다.
3 2번 과정을 지속하면서 개수를 세고, 상황에 따라 중앙값을 업데이트한다.
3-1 개수가 M보다 작은 경우 >> 현재 블루레이의 크기가 크다는 얘기이므로 크기를 줄인다.
3-2 개수가 M보다 큰 경우 >> 현재 블루레이의 크기가 작다는 얘기이므로 크기를 키운다.
4 위 과정을 반복한다.
"""
lb, ub = max(arr), 10 ** 10 + 1

while lb <= ub:
    middle = (lb + ub) // 2

    cnt = 0
    mem = 0
    flag = False
    for e in arr:
        if e > middle:
            flag = True
            break

        if mem + e <= middle:
            mem += e
        else:
            if mem:
                cnt += 1
                mem = e

    if flag:
        lb = middle + 1
        continue

    if mem:
        if mem <= middle:
            cnt += 1
        else:
            lb = middle + 1
            continue

    if cnt <= M:
        ub = middle - 1
    else:
        lb = middle + 1

print(lb)
