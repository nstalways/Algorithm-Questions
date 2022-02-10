# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램
# 시간 제한: 2초

N = int(input()) # 수의 개수

m = 0 # 약수의 개수
n = 0 # 소수의 개수

# 알고리즘
if 0 <= N <= 100:
    num_list = list(map(int, input().split()))

    if len(num_list) == N:
        for num in num_list:
            if 1 <= num <= 1000:
                m = 0
                denomiator = num

                for _ in range(num):
                    remain = num % denomiator

                    if remain == 0: # 나머지가 0이면 (약수이면)
                        m += 1
                    
                    denomiator -= 1

                if m == 2: # 소수는 약수의 개수가 1과 나 자신, 2개 밖에 없으므로
                    n += 1
            
            else:
                print('입력 숫자는 1,000 이하의 자연수이어야 합니다.')
                exit()
        
        print(n)
    else:
        print('입력한 값이 서로 맞지 않습니다.')
else:
    print('수의 개수는 100 이하입니다.')