# 골드바흐의 추측
# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다. 이러한 수를 골드바흐 수라고 한다.
# 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
# ex) 4 = 2 + 2 / 6 = 3 + 3 / 8 = 3 + 5 / 10 = 5 + 5 / 12 = 5 + 7 ...
# 10,000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성.
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력.
# 입력: 첫째 줄에 테스트 케이스의 개수 T가 주어짐. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어짐.
# 출력: 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력. 출력하는 소수는 작은 것부터 먼저 출력, 공백으로 구분.
# 제한: 4 <= n <= 10,000
# 시간 제한: 2초

from math import *
import time

# 입력
data = []

T = int(input())
for _ in range(T):
    data.append(int(input()))

# 알고리즘 (소수 리스트를 미리 만들고, 가능한 조합을 찾아보기)
start = time.time()

def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, ceil(sqrt(a)) + 1):
        if (a % i == 0) and (a != 2):
            return False
    return True

number = list(range(2, 10**(4) + 1))
prime_list = []

# 소수를 판별
for i in number:
    if isPrime(i):
        prime_list.append(i)

# 조합 찾기
comb_dict = {}

for idx, prime in enumerate(prime_list):
    for j in range(idx, len(prime_list)):
        hap = prime + prime_list[j]

        if ((hap % 2) == 0) and (hap <= 10**(4)): # 합이 짝수이면서, 10,000 이하인경우만
            cha = prime_list[j] - prime
            comb_info = (prime, prime_list[j], cha)

            if (hap in comb_dict) == False: # 새로운 값일 경우
                comb_dict[hap] = comb_info
            else: # 새로운 값이 아닌 경우
                if cha < comb_dict[hap][-1]:
                    comb_dict[hap] = comb_info

comb_dict = dict(sorted(comb_dict.items()))

# 입력 값의 파티션 출력하기
for x in data:
    part1 = comb_dict[x][0]
    part2 = comb_dict[x][1]
    print(part1, part2)

end = time.time()
print(f'Working Time: {end - start}')