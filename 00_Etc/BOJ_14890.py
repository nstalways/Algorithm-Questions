import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0

def is_road(heights):
    flag = True

    memo = [False] * N
    prev = heights[0]
    for i in range(1, N):
        cur = heights[i]
        diff = prev - cur

        if diff == 0:
            continue

        elif diff == -1:
            if i - L < 0:
                flag = False
                break
            else:
                tmp = memo[:]
                for j in range(i - L, i):
                    if memo[j]:
                        flag = False
                        break
                    else:
                        tmp[j] = True
                        if j + 1 == i:
                            memo = tmp

        elif diff == 1:
            if i + L > N:
                flag = False
                break
            else:
                tmp = memo[:]
                for j in range(i, i + L):
                    if memo[j]:
                        flag = False
                        break
                    else:
                        tmp[j] = True
                        if j + 1 == i + L:
                            memo = tmp

        else:
            flag = False
            break

        prev = cur

    return flag

# 행방향 탐색
for row in board:
    if is_road(row):
        ans += 1

# 열방향 탐색
for col in zip(*board):
    if is_road(col):
        ans += 1

print(ans)
