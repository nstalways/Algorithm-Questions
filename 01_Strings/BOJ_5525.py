import sys
input = sys.stdin.readline

# 입력
N = int(input().strip()) # 1 이상 100만 이하
M = int(input().strip()) # 2N + 1 이상 100만 이하
S = input().strip()

# 풀이
"""
I와 O가 교대로 나오는 문자열을 P_N이라고 한다.
주어진 문자열 S안에 P_N이 몇 군데 포함되어 있는지 구해야 한다.
P_N은 IOIOI ... 와 같은 형식으로 만들어진다.
>> N이 주어졌기 때문에, P_N을 구할 수 있다.
>> S에서 I가 발견된다면, I의 위치부터 탐색을 진행한다.
>> P_N과 동일하다면 횟수를 1 증가시킨다.
>> P_N과 다르다면 건너뛴다.

** 위 풀이는 시간 초과가 발생한다. 시간 복잡도가 대략 O(N**2)이기 때문.
** N이 100만이므로, O(N) 정도의 복잡도를 갖는 알고리즘을 설계해야 한다.
>> 정규식을 사용하는 풀이가 가장 간단할 듯 한다.

** 정규식의 경우, 겹치지 않는 경우만 찾아낼 수 있다.
>> 재귀적으로 풀어보자.

** 재귀적으로 접근 시 오히려 소요되는 시간이 늘어난다.
>> 겹치는 부분에 대해서도 판별을 해야하기 때문에, 중복되는 연산을 줄이는 방향으로 알고리즘을 설계해야 한다.
>> deque를 사용해보자.
"""
from collections import deque

S = deque(list(S))
queue = deque()

cnt = 0
while S:
    ch = S.popleft()

    if queue:
        if queue[-1] != ch:
            queue.append(ch)
        else:
            if queue[-1] == 'I':
                queue = deque(['I'])
            else:
                queue = deque()
    else:
        if ch == 'I':
            queue.append(ch)

    if len(queue) == 2*N + 1:
        cnt += 1
        for _ in range(2):
            queue.popleft()

print(cnt)
