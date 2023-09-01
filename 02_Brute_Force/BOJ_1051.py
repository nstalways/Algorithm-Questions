import sys

def solution(shape, rectangle):
    n, m = shape

    # 예외처리
    if n == 1 or m == 1:
        print(1)
        return
    
    # 모든 위치에서 가능한 경우의 수를 탐색한다
    # 배열의 크기를 벗어나지 않는다면, 시작 위치에서 위/아래로 같은 값을 더해서 확인한다.
    answer = float('-inf')
    for offset in range(0, min(n, m)):
        for i in range(n):
            for j in range(m):
                left_upper = rectangle[i][j]

                if (i + offset) >= n or (j + offset) >= m:
                    continue

                right_upper = rectangle[i + offset][j]
                right_lower = rectangle[i][j + offset]
                left_lower = rectangle[i + offset][j + offset]

                if (left_upper == right_upper) and (right_upper == right_lower)\
                    and (right_lower == left_lower):
                    answer = max(answer, (offset + 1) ** 2)
    
    print(answer)


if __name__ == "__main__":
    N, M = map(int, input().split())

    rectangle = []
    for _ in range(N):
        rectangle.append(list(map(int, list(sys.stdin.readline().strip()))))

    solution((N, M), rectangle)
    