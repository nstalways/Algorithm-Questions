# 베르트랑 공준
# 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다.
# goal: 자연수 n이 주어졌을 때, n보다 크고 2n보다 같거나 작은 소수의 개수를 구하는 프로그램을 작성.
# 입력: 테스트 케이스 여러개, 입력의 마지막에 0이 주어지면 입력을 그만둠.
# 출력: 각 테스트 케이스에 대해서 n보다 크고 2n보다 작거나 같은 소수의 개수를 출력.
# 제한: 1 <= n <= 123,456
# 시간 제한: 1초

from math import *
import time

# 입력
input_data = []

while True:
    tmp = int(input())
    if tmp == 0:
        break
    input_data.append(tmp)

start = time.time()

final_num = 123456

def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, ceil(sqrt(a)) + 1):
        if (a % i == 0) and (a != 2):
            return False
    return True

data = list(range(2, 2*final_num + 1))
prime_list = []

# 소수를 판별
for i in data:
    if isPrime(i):
        prime_list.append(i)

for n in input_data:
    output = 0
    
    for ii in prime_list:
        if ii > n and ii <= 2*n:
            output += 1
    
    print(output)

end = time.time()
print(f'Working Time: {end - start}')