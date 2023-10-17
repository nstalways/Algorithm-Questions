import sys

def solution(s1, s2):
    n, m = len(s1), len(s2)
    lcs = [[0] * (m + 1) for _ in range(n + 1)]
    
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            ch1, ch2 = s1[i - 1], s2[j - 1]

            if ch1 != ch2:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
            else:
                lcs[i][j] = lcs[i - 1][j - 1] + 1

            ans = max(ans, lcs[i][j])
    
    print(ans)


if __name__ == "__main__":
    input = sys.stdin.readline

    s1 = input().strip()
    s2 = input().strip()

    solution(s1, s2)
