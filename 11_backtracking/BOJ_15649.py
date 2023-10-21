import sys
from itertools import permutations

def solution(n, m):
    num_lst = [str(i) for i in range(1, n + 1)]
    res = set(permutations(num_lst, m))
    ans = sorted([' '.join(list(tmp)) for tmp in res])

    print(*ans, sep='\n')

def solution2(n, m):
    """backtracking"""
    ans = []

    def backtracking():
        if len(ans) == m:
            print(' '.join(map(str, ans)))
            return
        
        for i in range(1, n + 1):
            if i not in ans:
                ans.append(i)
                backtracking()
                ans.pop()

    backtracking()


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    # solution(N, M)
    solution2(N, M)
