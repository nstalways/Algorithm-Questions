def solution(N):
    # 예외처리
    if N <= 2:
        print(1)
        return

    dp = [[] for _ in range(N)]
    dp[0] = [0, 1] # pinary number의 마지막 숫자가 (0인 숫자의 개수, 1인 숫자의 개수)
    dp[1] = [1, 0]

    for pos in range(2, N):
        fin_w_zero, fin_w_one = dp[pos - 1]

        dp[pos].extend([fin_w_zero + fin_w_one, fin_w_zero])
    
    print(sum(dp[N - 1]))
            

if __name__ == "__main__":
    N = int(input())

    solution(N)
