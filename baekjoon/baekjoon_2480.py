# 1 ~ 6 주사위 3개를 던져 규칙에 따라 상금을 받는 게임
# 같은 눈이 3개가 나오면 10,000원 + (같은 눈) x 1000원의 상금 수여
# 같은 눈이 2개만 나오면 1,000원 + (같은 눈) x 100원의 상금 수여
# 모두 다른 눈이 나오면 (그 중 가장 큰 눈) x 100원의 상금 수여
# 3개 주사위의 눈이 주어졌을 때 상금을 계산하는 프로그램 구현
# 입력: 3개의 눈이 빈칸을 사이에 두고 각각 주어짐
# 출력: 게임의 상금
# 시간 제한: 1초

# 함수
def print_reward(num):
    print(10**(3) + num * 10**(2))

# 입력
data = input()
A = int(data.split()[0])
B = int(data.split()[1])
C = int(data.split()[2])

# 알고리즘
if (1 <= A <= 6) and (1 <= B <= 6) and (1 <= C <= 6):
    # 모두 다른 눈인 경우
    if (A != B) and (B != C) and (A != C):
        print(max(A, B, C) * 10**(2))
    # 모두 같은 눈인 경우
    elif (A == B) and (B == C) and (A == C):
        print(10**(4) + (A * 10**(3)))
    # 같은 눈이 2개만 나오는 경우
    else:
        if A == B:
            print_reward(A)
        elif B == C:
            print_reward(B)
        else:
            print_reward(C)

else:
    print('주사위의 눈은 1 이상 6 이하의 숫자입니다.')