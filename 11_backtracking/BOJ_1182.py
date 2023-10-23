import sys

def solution(N, S, integer_lst):
    cnt = 0
    tmp = []

    def backtracking(start):
        nonlocal cnt
        print(start, tmp)
        if tmp and sum(tmp) == S:
            cnt += 1
            return
        
        for i in range(start, N):
            tmp.append(integer_lst[i])
            backtracking(i + 1)
            tmp.pop()
    
    backtracking(0)
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
    # basic_solution(N, S, integer_lst)
