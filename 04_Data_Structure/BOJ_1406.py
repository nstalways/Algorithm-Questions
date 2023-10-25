import sys
from collections import deque

def solution(init_s, M, cmds):
    q1 = deque(init_s)
    q2 = deque([])

    for cmd in cmds:
        tmp = cmd[0]
        if tmp == 'L':
            if q1:
                q2.appendleft(q1.pop())
        elif tmp == 'D':
            if q2:
                q1.append(q2.popleft())
        elif tmp == 'B':
            if q1:
                q1.pop()
        else:
            q1.append(cmd[1])

    res = ''.join(list(q1) + list(q2))
    print(res)
    

if __name__ == "__main__":
    input = sys.stdin.readline

    init_s = list(input().strip()) # 길이 N, 영어 소문자, 10만 이하
    M = int(input().strip())

    cmds = []
    for _ in range(M):
        cmds.append(input().split())

    solution(init_s, M, cmds)
