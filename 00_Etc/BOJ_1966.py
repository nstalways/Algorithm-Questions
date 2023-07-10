import sys
from collections import deque


def solution(n, m, priorities):
    priorities = deque([(i, p) for i, p in enumerate(priorities)])

    # 예외처리
    if len(priorities) == 1:
        return 1
    
    cnt_order = 0
    while priorities:
        curr = priorities.popleft()

        if priorities and curr[1] < max(priorities, key=lambda x: x[1])[1]:
            priorities.append(curr)
            continue
        
        cnt_order += 1

        if curr[0] == m:
            break


    return cnt_order


if __name__ == "__main__":
    # 입력
    T = int(input())

    answer = []
    for _ in range(T):
        N, M = map(int, input().split())
        priorities = list(map(int, sys.stdin.readline().strip().split()))

        answer.append(solution(N, M, priorities))
    
    # 출력
    for a in answer:
        print(a)
