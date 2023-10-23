import sys

def solution(N, S, integer_lst):
    cnt = 0

    def backtracking():
        nonlocal cnt

        if len(tmp) == lim:
            res = 0
            for i in tmp:
                res += integer_lst[i]
            
            if res == S:
                cnt += 1
            
            return

        for i in range(N):
            if not tmp:
                tmp.append(i)
            else:
                if i > tmp[-1]:
                    tmp.append(i)
                else:
                    continue
            
            backtracking()
            tmp.pop()

    for i in range(1, N + 1):
        tmp = []
        lim = i
        backtracking()

    print(cnt)

from itertools import combinations

def basic_solution(N, S, integer_lst):
    """backtracking보다 훨씬 빠름"""
    cnt = 0
    for select in range(1, N + 1):
        candidates = list(combinations(integer_lst, select))

        for candidate in candidates:
            if sum(candidate) == S:
                cnt += 1
    
    print(cnt)


if __name__ == "__main__":
    input = sys.stdin.readline

    N, S = map(int, input().split())
    integer_lst = list(map(int, input().split()))

    solution(N, S, integer_lst)
    basic_solution(N, S, integer_lst)
