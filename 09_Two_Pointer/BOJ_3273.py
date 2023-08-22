import sys


def solution(num_lst, target_num):
    # 정렬
    num_lst = sorted(num_lst)

    # 투 포인터 사용
    left, right = 0, len(num_lst) - 1

    cnt = 0
    while left < right:
        num1, num2 = num_lst[left], num_lst[right]

        if num1 + num2 == target_num:
            cnt += 1
            left += 1
            right -= 1
            continue

        if num1 + num2 < target_num:
            left += 1
        else:
            right -= 1

    print(cnt)


if __name__ == "__main__":
    n = int(input())
    num_lst = list(map(int, sys.stdin.readline().split()))
    target_num = int(input())

    solution(num_lst, target_num)
