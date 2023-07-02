# 이 문제는 왜 DP일까..?
def solution(num_stones):
    if num_stones % 2 == 0:
        print("CY")
    else:
        print("SK")


if __name__ == "__main__":
    # 입력
    N = int(input())

    solution(N)
