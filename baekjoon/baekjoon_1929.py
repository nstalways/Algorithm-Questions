# 에리토스테네스의 체
from math import *

# 입력
tmp = input()
M = int(tmp.split()[0])
N = int(tmp.split()[1])

# 알고리즘
if 1 <= M <= N <= 10**(6):
    prime_num_list = []

    square_root = ceil(sqrt(N)) # 가장 가까운 제곱근 구하기

    # 에리토스테네스의 체를 적용하기 위해서, 제곱근 내의 소수 구하기
    for i in range(square_root):
        numerator = i + 1
        denomiator = 1
        cnt = 0
        
        for j in range(numerator):
            remain = numerator % denomiator
        
            if denomiator > int(numerator // 2):
                cnt += 1
                break
            if remain == 0: # 약수면
                cnt += 1
            if cnt > 2: # 소수가 아니면
                break

            denomiator += 1
        
        if cnt == 2: # 소수이면
            prime_num_list.append(numerator)

    # 에리토스테네스의 체
    for x in range(N - M + 1):
        tmp = 0
        val = M + x
        
        for prime_num in prime_num_list:
            if val == prime_num:
                print(val)
                break
            if (val % prime_num) == 0:
                break
            tmp += 1
        
        if (tmp == len(prime_num_list)) and (val != 1):
            print(val)

else:
    print('주어진 조건에 맞게 값을 입력해주세요.')