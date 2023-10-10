import sys

def solution(a, k):
    a_tmp = a[::-1]
    balance = k
    ans = 0
    for value in a_tmp:
        if not balance:
            break

        if value > balance:
            continue

        num_coin, balance = divmod(balance, value)
        ans += num_coin

    print(ans)


if __name__ == "__main__":
    input = sys.stdin.readline

    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input().strip()))

    solution(A, K)
