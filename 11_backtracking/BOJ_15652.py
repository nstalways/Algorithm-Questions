def solution(N, M):
    tmp = []
    def backtracking():
        if len(tmp) == M:
            print(' '.join(map(str, tmp)))
            return
        
        for i in range(1, N + 1):
            if not tmp:
                tmp.append(i)
                
            else:
                if tmp[-1] <= i:
                    tmp.append(i)
                else:
                    continue

            backtracking()
            tmp.pop()
        
    backtracking()


if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)
