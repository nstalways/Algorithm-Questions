import sys
from collections import deque
input = sys.stdin.readline

# 입력
T = int(input().strip())

# 풀이
"""
'-': 커서의 바로 앞에 글자가 존재하는 경우, 글자를 지우는 명령
'<, >': 화살표의 입력으로, 커서의 위치를 움직일 수 있다면 왼쪽 또는 오른쪽으로 1만큼 움직임
* 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동

커서 위치가 바뀐 상태에서 문자를 입력할 때 발생할 수 있는 복사 등을 줄이는 것이 문제의 핵심
>> 커서 위치를 기준으로 좌/우를 구분하여 입력받는다
"""
def solution(_logs):
    left, right = [], deque()
    for log in _logs:
        if log == '<':
            if not left:
                continue

            right.appendleft(left.pop())

        elif log == '>':
            if not right:
                continue

            left.append(right.popleft())

        elif log == '-':
            if not left:
                continue

            left.pop()

        else:
            left.append(log)

    return ''.join(left + list(right))


ans = []
for _ in range(T):
    logs = input().strip()
    res = solution(logs)

    ans.append(res)

print(*ans, sep='\n')