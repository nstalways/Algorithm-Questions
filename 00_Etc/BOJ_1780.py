import sys
from collections import deque


def check(arr):
    base = arr[0][0]
    state = True

    for row in arr:
        for element in row:
            if base != element:
                state = False
                break
        
        if not state:
            break

    return state, base


def split(arr):
    result = []

    for i in range(0, len(arr), len(arr) // 3):
        stack = []
        for row in arr:
            stack.append(row[i:i + len(row) // 3])

            if len(stack) == len(row) // 3:
                result.append(stack)
                stack = []           
    
    return result


# deque 풀이 -> 메모리 초과
def solution(arr):
    answer = [0] * 3
    queue = deque([arr])

    while queue:
        curr = queue.popleft()
        state, base = check(curr)

        if state:
            answer[base + 1] += 1
        else:
            if len(curr) == 1:
                answer[curr[0] + 1] += 1
                continue

            queue.extend(split(curr))

    for a in answer:
        print(a)


# 재귀함수를 이용한 풀이 -> 통과
def solution2(arr):
    answer = [0] * 3
    
    def recursive_call(arr):
        state, base = check(arr)
        
        if state:
            answer[base + 1] += 1
            return
        else:
            for matrix in split(arr):
                recursive_call(matrix)
    
    recursive_call(arr)

    for a in answer:
        print(a)


if __name__ == "__main__":
    # 기본 세팅
    sys.setrecursionlimit(10**6)

    # 입력
    N = int(input())
    
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, sys.stdin.readline().strip().split())))
    
    solution2(matrix)
    