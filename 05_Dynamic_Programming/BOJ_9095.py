def solution(num_list):
    dp = [0, 1, 2, 4, 7]

    # 11까지 조합을 미리 구해서 dp 테이블에 저장
    for idx in range(len(dp), 11 + 1):
        dp.append(dp[idx - 3] + dp[idx - 2] + dp[idx - 1])

    for num in num_list:
        print(dp[num])
    

if __name__ == "__main__":
    # 입력
    T = int(input())
    num_list = [int(input()) for _ in range(T)]

    solution(num_list)
    