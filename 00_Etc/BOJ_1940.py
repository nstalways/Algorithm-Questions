import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
M = int(input().strip())
arr = list(map(int, input().split()))

# 풀이
"""
갑옷은 "두 개의 재료"로 만든다. + 각 재료는 고유한 번호를 가진다.
>> 고유 번호 배열을 선언하고, 입력받은 재료의 번호를 1로 표시
>> 처음부터 순서대로 탐색하면서, M - arr[i]를 검색했을 때 1이라면 횟수 증가, 0이면 무시
"""
ingredients = [0] * (100000 + 1)
for e in arr:
    ingredients[e] = 1

ans = 0
for e in arr:
    ingredients[e] = 0

    if e >= M:
        continue
    else:
        remain = M - e
        try:
            if ingredients[remain]:
                ingredients[remain] = 0
                ans += 1
        except:
            pass

print(ans)
