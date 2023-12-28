import sys
input = sys.stdin.readline

# 풀이
"""
조합을 이용한 풀이
- 주어진 숫자 집합에서 6개의 숫자를 고르는 모든 조합을 구한 뒤 출력

백트래킹을 이용한 풀이
- 재귀와 stack을 이용
- stack에 들어있는 숫자 개수가 6개인 경우, 출력
"""
def combination_solution():
    from itertools import combinations

    while True:
        arr = list(map(int, input().split()))
        if arr[0] == 0:
            break

        data = arr[1:]
        combs = list(combinations(data, 6))
        for comb in combs:
            print(*comb)

        print()

def backtracking_solution():
    def backtracking(idx):
        if len(stack) == 6:
            print(*stack)
            return

        for i in range(idx, k):
            if stack and data[i] <= stack[-1]:
                continue

            stack.append(data[i])
            backtracking(idx + 1)
            stack.pop()

    while True:
        arr = list(map(int, input().split()))
        if arr[0] == 0:
            break

        k, data = arr[0], arr[1:]
        stack = []

        backtracking(0)
        print()


if __name__ == "__main__":
    backtracking_solution()