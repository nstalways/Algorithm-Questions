# 입력
N = int(input())
candidates = [int(input()) for _ in range(N)]

# 풀이
def solution():
    # 예외 처리
    if N == 1:
        print(0)
        return

    ans = 0
    me, others = candidates[0], candidates[1:]

    while True:
        others.sort(reverse=True)
        if me > others[0]:
            print(ans)
            break

        others[0] -= 1
        me += 1

        ans += 1

solution()
