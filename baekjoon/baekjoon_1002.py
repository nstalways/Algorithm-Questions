# 시간 제한: 2초
import math, sys

data = []
T = int(input())

for _ in range(T):
    data.append(list(map(int, input().split())))

for val in data:
    x_1, y_1, r_1, x_2, y_2, r_2 = val[0], val[1], val[2], val[3], val[4], val[5]

    flag1 = [-10**4 <= x <= 10**4 for x in [x_1, y_1, x_2, y_2]]
    flag2 = [1 <= y <= 10**4 for y in [r_1, r_2]]
    flag = flag1 + flag2

    if flag == [True]*6:
        distance1 = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
        distance2 = math.sqrt(r_1**2 + r_2**2)
        sum_rad = r_1 + r_2

        outer_flag = (math.fabs(distance1 - sum_rad) <= sys.float_info.epsilon)
        inner_flag = (math.fabs(distance1 - abs(r_1 - r_2)) <= sys.float_info.epsilon)

        # print(f'distance1: {distance1}')
        # print(f'distance2: {distance2}')
        # print(f'sum_rad: {sum_rad}')
        # print(f'case_flag: {case_flag}')

        # case 1: 무한 개인 경우 (일치)
        if (x_1, y_1, r_1) == (x_2, y_2, r_2):
            print(-1)
        # case 2: 0개인 경우 (두 원이 서로 안 만나는 경우)
        elif (sum_rad < distance1) or (distance1 < abs(r_2 - r_1)):
            print(0)
        # case 3: 1개인 경우 (한 점에서 만나는 경우(외접 or 내접))
        elif inner_flag or outer_flag:
            print(1)
        # case 4: 2개인 경우
        else:
            print(2)

    else:
        print('주어진 조건에 맞게 값을 입력해주세요.')
