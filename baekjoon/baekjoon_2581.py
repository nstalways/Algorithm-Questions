# 자연수 M과 N이 주어질 때, M 이상 N 이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 구현하라.
# 입력의 첫째 줄에 M과 N이 주어짐.
# M과 N은 10,000 이하의 자연수이고, M은 N보다 작거나 같음.
# 첫째 줄엔 합을, 둘째 줄엔 최솟값을 출력. 소수가 없을 경우 첫째 줄에 -1을 출력.
# 시간 제한: 1초

# 입력
M = int(input())
N = int(input())

if (1 <= M <= 10**4) and (1 <= N <= 10**4) and (M <= N):
    # 관련 변수
    num = M
    prime_number_list = []

    # 알고리즘
    for i in range(N - M + 1):
        denomiator = 1
        divisor = 0

        # 소수인지 판별하는 구문
        for _ in range(num):
            remain = num % denomiator

            if remain == 0: # 나머지가 0 (=약수라는 뜻)
                divisor += 1
            
            if divisor > 2: # 약수가 2개 이상이면 (=num이 소수가 아님)
                break # 반복문 탈출

            denomiator += 1
        
        if divisor == 2: # 두 번째 반복문을 다 돌고, 약수가 2개면 (=소수라는 뜻)
            prime_number_list.append(num)
        
        num += 1

    if len(prime_number_list) == 0:
        print(-1)
        exit()
    else:
        print(sum(prime_number_list))
        print(min(prime_number_list))
else:
    print('주어진 조건을 만족하는 값을 입력해주세요.')