import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
infos = list(map(int, input().split()))
k = int(input().strip())

# 풀이
"""
구현
순서대로 정렬할 필요없이, k명의 회원이 정렬할 때 결과를 바로 출력하면 됨.
이전 단계의 정렬 상태와 관계없이, k명의 회원이 정렬할 때 범위 내 모든 치킨집을 확인해야하기 때문
k = n // x -> x = n // k-> x: k명의 회원이 정렬할 치킨집의 수
"""
factor = N // k
for i in range(0, N, factor):
    print(*sorted(infos[i:i + factor]), end= ' ')
