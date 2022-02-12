# 정수 N이 주어졌을 때, 소인수분해하는 프로그램 작성
# 입력: 정수 N (1 이상 10,000,000 이하)
# N의 소인수 분해 결과를 한 줄에 하나씩 오름차순으로 출력.
# N이 1일 경우 아무것도 출력하지 않음.
# 시간 제한: 1초

# 입력
N = int(input())

# 알고리즘
if 1 <= N <= 10**(7):
    flag = True
    divisor = 2

    if N == 1:
        pass
    else:
        while flag:
            remain = N % divisor
            
            if remain == 0: # 약수라면
                print(divisor)
                N = int(N//divisor)
            else:
                divisor += 1
            
            if N == 1:
                flag = False
                
else:
    print('N은 1 이상 10,000,000 이하의 정수입니다.')