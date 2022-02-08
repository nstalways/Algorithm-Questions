# 사탕가게에 설탕을 정확히 N Kg만큼 배달해야 함.
# 설탕은 봉지에 담겨져 있고, 봉지의 종류는 3 Kg, 5 Kg 두 종류이다.
# 최대한 적은 수의 봉지를 사용하려 한다.
# 시간 제한: 1초

N = int(input())

num_3 = 0
num_5 = 0

def divide_3(N):
    tmp = N // 3
    tmp2 = N - (tmp * 3)
    
    return tmp, tmp2

def divide_5(N):
    tmp = N // 5
    tmp2 = N - (tmp * 5)
    
    return tmp, tmp2

# 알고리즘
if 3 <= N <= 5000:
    # 5 Kg을 쓰는 게 최선이므로, 먼저 확인
    num_5, remain_5 = divide_5(N)
    if remain_5 == 0: # 남지 않는다면
        print(num_5)
    else: #남으면
        num_3, remain_3 = divide_3(remain_5) # 나머지가 3Kg로 딱 떨어지는지 확인
        if remain_3 == 0: # 딱 떨어지면
            print(num_5 + num_3)
        else: # 딱 안 떨어지면
            tmp_5 = num_5
            # 우선 5Kg 봉지를 줄여가면서 확인
            for _ in range(num_5):
                tmp_5 -= 1
                tmp_remain_5 = N - (tmp_5 * 5)
                tmp_3, tmp_remain_3 = divide_3(tmp_remain_5)
                if tmp_remain_3 == 0: # 5Kg 개수를 줄였을 때 딱 떨어지면
                    print(tmp_5 + tmp_3)
                    exit()
                else: # 그래도 안되면
                    continue
            
            # 5Kg 개수를 줄였는데도 안되면
            num_3, remain_3 = divide_3(N)
            if remain_3 == 0: # 딱 떨어지면
                print(num_3)
            else:
                print(-1)
   
else:
    print('입력 값은 3 이상 5000 이하의 자연수입니다.')