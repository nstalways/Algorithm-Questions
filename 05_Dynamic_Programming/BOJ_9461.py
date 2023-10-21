def solution(n):
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n <= 10:
        return dp[n - 1]
    
    for _ in range(n - 10):
        dp.append(dp[-1] + dp[-5])
    
    return dp[-1]


if __name__ == "__main__":
    T = int(input())
    
    ans = []
    for _ in range(T):
        res = solution(int(input()))
        ans.append(res)

    print(*ans, sep='\n')
