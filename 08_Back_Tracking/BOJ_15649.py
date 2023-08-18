from itertools import permutations


# Solve
def solution(n, m):
    seq_lst = sorted(set(permutations([str(x) for x in range(1, n + 1)], m)))
    
    for seq in seq_lst:
        print(' '.join(seq))


# Study
def backtracking(n, m):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    for num in range(1, n+1):
        if num not in answer:
            answer.append(num)
            backtracking(n, m)
            answer.pop() # 제거


if __name__ == "__main__":
    N, M = map(int, input().split())

    # solution(N, M)
    answer = []
    backtracking(N, M)
