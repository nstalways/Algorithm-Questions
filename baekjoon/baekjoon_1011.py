# k만큼 이동했을 때, 다음은 k-1, k, k+1 만큼만 이동할 수 있음.
# 초기 작동 시, 1만큼만 이동할 수 있음.
# x 지점에서 y 지점으로 이동할 때, 최소한의 작동 횟수로 이동해야 함.
# y 지점에 도착하기 바로 직전의 이동거리는 1로 고정되어 있음.
# x는 항상 y보다 작은 값을 가짐.
# 시간 제한: 2초

from math import *

# 테스트 케이스의 개수
T = int(input())

# 입력
data = []

for _ in range(T):
    tmp1 = input() # ex) 1 2
    data.append(list(map(int, tmp1.split())))

# 알고리즘
for val in data:
    step = 0
    x = int(val[0])
    y = int(val[1])

    if 0 <= x < y < 2**(31):
        distance = y - x
        n = round(sqrt(float(distance))) # 가장 가까운 제곱근 구하기
        if distance <= n**2: # distance가 n 제곱보다 같거나 작을 경우
            step = (2 * n) - 1
        else:
            step = 2 * n
        
        print(step)
    else:
        print('조건에 맞춰 값을 입력해주세요.')