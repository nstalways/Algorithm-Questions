# 입력
S = int(input())

# 풀이
"""
*서로 다른 N개*의 자연수를 합하면 S
S를 알 때 자연수 N의 최댓값 -> 개수를 최대로
개수를 최대로 -> 작은 숫자를 최대한 많이 쓴다 -> 등차수열 이용
"""
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