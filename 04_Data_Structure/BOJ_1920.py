import sys

def solution(a, b):
    remain = set(b) - set(a)
    ans = [0 if tmp in remain else 1 for tmp in b]

    print(*ans, sep='\n')


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    A = list(map(int, input().split()))
    M = int(input().strip())
    B = list(map(int, input().split()))

    solution(A, B)
    