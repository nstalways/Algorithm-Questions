import sys

def solution(num_stairs, scores):
    """
    총 계단 개수만큼 dp 배열을 생성한다.
    dp 배열에는 각 계단을 밟을 때까지 최고 점수를 기록한다.
    """
    if num_stairs == 1:
        print(scores[0])
        return 

    dp = [0] * (num_stairs + 1)
    dp[1] = scores[0]
    dp[2] = dp[1] + scores[1]

    for i in range(3, num_stairs + 1):
        dp[i] = max(dp[i - 3] + scores[i - 2] + scores[i - 1],
                    dp[i - 2] + scores[i - 1])

    print(dp[num_stairs])


if __name__ == "__main__":
    input = sys.stdin.readline

    num_stairs = int(input().strip()) # <= 300 자연수
    scores = [] # score <= 10,000 자연수
    for _ in range(num_stairs):
        scores.append(int(input().strip()))

    solution(num_stairs, scores)
