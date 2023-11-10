# 입력
S = int(input())

# 풀이
"""
*서로 다른 N개*의 자연수를 합하면 S
S를 알 때 자연수 N의 최댓값 -> 개수를 최대로
개수를 최대로 -> 작은 숫자를 최대한 많이 쓴다 -> 등차수열 이용
"""
def solution1():
    a, l = 1, 1
    ans = 1

    while True:
        n = l - a + 1
        tmp = (n * (l + a)) / 2

        if tmp >= S:
            print(ans)
            break

        if a <= S - tmp <= l:
            pass
        else:
            ans = n + 1

        l += 1

def solution2():
    """solution1 대비 약 2배 빠름
    """
    if S <= 2:
        print(1)
        return

    tmp = 0
    a = 1
    n = 0

    ans = 0
    while True:
        tmp += a
        n += 1

        if tmp >= S:
            print(ans)
            break

        if S - tmp > a:
            ans = n + 1

        a += 1

solution1()
solution2()