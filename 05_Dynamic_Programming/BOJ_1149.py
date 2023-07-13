import sys


def solution(house_list):
    # R, G, B 별 최솟값 저장
    dp = house_list[0]
    for level in range(1, len(house_list)):
        min_r = house_list[level][0] + min(dp[1], dp[2])
        min_g = house_list[level][1] + min(dp[0], dp[2])
        min_b = house_list[level][2] + min(dp[0], dp[1])

        dp = [min_r, min_g, min_b]

    print(min(dp))


if __name__ == "__main__":
    # 입력
    house_list = []
    for _ in range(int(input())):
        house_list.append(list(map(int, sys.stdin.readline().strip().split())))
    
    solution(house_list)
    