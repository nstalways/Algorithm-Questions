def basic_solution(n, m):
    from itertools import combinations

    res = sorted(list(combinations([i for i in range(1, n + 1)], m)))
    ans = [' '.join(map(str, tmp)) for tmp in res]
    print(*ans, sep='\n')


def solution(n, m):
    ans = []

    def backtracking():
        if len(ans) == m:
            print(' '.join(map(str, ans)))
            return

        for i in range(1, n + 1):
            if not ans:
                ans.append(i)
            else:
                if i > ans[-1]:
                    ans.append(i)
                else:
                    continue
            
            backtracking()
            ans.pop()

    backtracking()


if __name__ == "__main__":
    N, M = map(int, input().split())

    basic_solution(N, M)
    solution(N, M)
