import sys
from math import factorial

def solution(n, m):
    return factorial(m) // (factorial(m - n) * factorial(n))


if __name__ == "__main__":
    input = sys.stdin.readline
    
    ans_per_case = []

    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().split())
        ans_per_case.append(solution(N, M))
    
    for ans in ans_per_case:
        print(ans)
