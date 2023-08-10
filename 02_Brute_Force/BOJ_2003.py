import sys


def solution(numbers, target_number):
    start, end = 0, 1

    hap, cnt = 0, 0
    while end <= len(numbers):
        hap = sum(numbers[start:end])

        if hap == target_number:
            cnt += 1
            start += 1
        elif hap < target_number:
            end += 1
        elif hap > target_number:
            start += 1

    print(cnt)


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, sys.stdin.readline().split()))

    solution(A, M)
