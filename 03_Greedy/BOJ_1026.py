import sys


# 정렬 이용해서 풀기 (문제 조건에는 위배됨)
def solution1(A, B):
    A, B = sorted(A), sorted(B, reverse=True)

    answer = 0
    for a, b in zip(A, B):
        answer += a * b
    
    print(answer)


if __name__ == "__main__":
    # 입력부
    N = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    solution1(A, B)
