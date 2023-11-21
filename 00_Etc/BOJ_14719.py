import sys
input = sys.stdin.readline

# 입력
H, W = map(int, input().split())
arr = list(map(int, input().split()))

# 풀이
"""
빗물이 고인다 -> 이 개념을 어떻게 코드로 구현할 것인가?
>> 투 포인터를 이용해보자.
>> pt1, pt2는 각각 현재 위치, 다음 위치를 의미한다.
>> pt1의 높이보다 pt2의 높이가 낮다면, pt2 증가 및 높이의 차이를 고인 빗물로 정의한다.
>> pt1의 높이와 pt2의 높이가 같거나 pt2가 더 높다면, pt1을 pt2로, pt2는 pt1 + 1로 정의해서 다시 탐색한다.
>> 배열을 끝까지 탐색했을 때, pt1과 같거나 그보다 높은 pt2가 존재하지 않는다면 0을 출력한다.
* 위 구현 방식은, "pt1보다 pt2의 높이가 낮음에도 빗물이 고이는 경우"를 처리하지 못한다.

탐색 문제라고 하기엔, 배열의 크기가 너무 크고 시간 제한이 빡세다.
2차원 입력을 준 이유가 있을 듯 한데,,
>> 비가 고이기 위해선, 양쪽 끝이 블록(1)이어야 한다.
>> H를 따라서 이차원 배열을 탐색하는데, 두 개의 블록이 나오면 그 사이 빈 칸을 고인 빗물로 정의한다.
>> 만약 두 개의 블록이 나오지 않는다면, 아무 값도 더하지 않는다.
"""
ans = 0
for r in range(H):
    h = H - r

    l_block, r_block = False, False
    tmp = 0
    for c in range(W):
        if h > arr[c]:
            if l_block:
                tmp += 1
        else:
            if (l_block, r_block) == (False, False):
                l_block = True
            elif (l_block, r_block) == (True, False):
                ans += tmp
                tmp = 0

print(ans)
