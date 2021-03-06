# 시작 시간, 요리에 필요한 시간이 분 단위로 주어졌을 때, 요리가 끝나는 시각을 계산하는 프로그램을 구현하라
# 입력: 첫째 줄 > 현재 시각 (시간:분), 둘째 줄 > 요리하는 데 필요한 시간 C
# 출력: 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력
# 시간 제한: 1초
# 조건: 0 <= A(시) <= 23, 0 <= B(분) <= 59

# 입력
time = input() # 현재 시간
C = int(input()) # 요리에 필요한 시간

A = int(time.split()[0])
B = int(time.split()[1])

# 알고리즘
if (0 <= A <= 23) and (0 <= B <= 59) and (0 <= C <= 10**(3)):
    tmp = 60 * A # 시간을 분 단위로 변환
    tmp += B # 현재 시각을 분으로 변환
    tmp += C # 현재 시각에 요리에 필요한 시간을 더함

    hour = int(tmp // 60) # 시간 계산
    minute = int(tmp % 60) # 분 계산

    if hour >= 24:
        hour -= 24
    
    print(hour, minute)    

else:
    print('주어진 조건에 맞게 값을 입력해주세요.')