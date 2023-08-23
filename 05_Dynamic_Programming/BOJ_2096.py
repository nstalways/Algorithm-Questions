# DP        
def solution(N):
    dp_for_min, dp_for_max = [0, 0, 0], [0, 0, 0]
    for _ in range(N):
        table = list(map(int, input().split()))

        # 최소 구하기
        dp_for_min = [
            table[0] + min(dp_for_min[0], dp_for_min[1]),
            table[1] + min(dp_for_min),
            table[2] + min(dp_for_min[1], dp_for_min[2])
        ]

        # 최대 구하기
        dp_for_max = [
            table[0] + max(dp_for_max[0], dp_for_max[1]),
            table[1] + max(dp_for_max),
            table[2] + max(dp_for_max[1], dp_for_max[2])
        ]
        
    print(max(dp_for_max), min(dp_for_min))


if __name__ == "__main__":
    N = int(input())

    solution(N)
