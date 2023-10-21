def solution(N, M):
    tmp = []
    def backtracking():
        if len(tmp) == M:
            print(' '.join(map(str, tmp)))
            return

        for i in range(1, N + 1):
            tmp.append(i)
            backtracking()
            tmp.pop()
    
    backtracking()


if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)
