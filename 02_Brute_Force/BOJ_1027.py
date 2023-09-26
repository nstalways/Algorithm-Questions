import sys
import math

def solution(height_of_buildings, n):
    ans = [0] * n

    def get_slope(w, h):
        return h / w

    for building, height in enumerate(height_of_buildings):
        cnt = 0
        
        # 왼쪽 빌딩 탐색
        slope = float('-inf')
        for i in range(building - 1, -1, -1):
            w, h = abs(building - i), height_of_buildings[i] - height
            new_slope = get_slope(w, h)

            if new_slope > slope:
                cnt += 1
                slope = new_slope

        # 오른쪽 빌딩 탐색
        slope = float('-inf')
        for i in range(building + 1, n):
            w, h = abs(i - building), height_of_buildings[i] - height
            new_slope = get_slope(w, h)

            if new_slope > slope:
                cnt += 1
                slope = new_slope

        ans[building] = cnt

    print(max(ans))


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    height_of_buildings = list(map(int, input().split()))

    solution(height_of_buildings, N)
