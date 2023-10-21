import sys

def solution(n, data):
    """
    dp 배열: 자기 자신을 포함한 현재까지 가장 긴 증가하는 부분 수열의 길이

    1. i번째 숫자와 i - 1번째 숫자까지 대/소 비교를 수행
    2. 더 큰 값이고, dp 배열에서 부분 수열의 길이 또한 더 길다면 값을 할당.
    3. 자기 자신을 추가
    """
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if data[i] > data[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    
    print(max(dp))


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    data = list(map(int, input().split()))

    solution(N, data)
