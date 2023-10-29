import math
import sys
input = sys.stdin.readline

# 배열 초기화
lim = 10 ** 6

is_prime = [1] * (lim + 1)
is_prime[0], is_prime[1] = 0, 0

# 1. 제곱근 내 소수 구하기
ub = int(math.sqrt(lim))
tmp = []
for numerator in range(2, ub + 1):
    cnt = 2
    for denomiator in range(2, int(numerator / 2) + 1):
        if cnt > 2:
            break

        if (numerator % denomiator) == 0:
            cnt += 1
    
    if cnt == 2:
        tmp.append(numerator)

# 2. 소수를 제외한 소수의 배수들을 걸러내기
for t in tmp:
    for i in range(t ** 2, lim + 1, t):
        is_prime[i] = 0

# 3. 골드바흐의 추측 검증
ans = []
while True:
    n = int(input().strip())
    if n == 0:
        print(*ans, sep='\n')
        break

    # 3. 골드바흐의 추측 검증
    is_wrong = True
    end = int(n / 2)
    for i in range(3, end + 1, 2):
        if is_prime[i] and is_prime[n - i]:
            is_wrong = False
            ans.append(f'{n} = {i} + {n - i}')
            break
    
    if is_wrong:
        ans.append("Goldbach's conjecture is wrong.")
