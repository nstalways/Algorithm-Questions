from sys import stdin

# 입력부
nums = []
while True:
    input_num = int(stdin.readline().strip())
    if input_num == -1:
        break
    
    nums.append(input_num)

for n in nums:
    # 약수 구하기
    divisors = [1, ]
    for denomiator in range(2, int(n/2) + 1):
        if (n % denomiator) == 0:
            divisors.append(denomiator)

    # 완전수 판별
    if n == sum(divisors):
        print(f'{str(n)} = ' + ' + '.join([str(x) for x in divisors]))
    else:
        print(f'{str(n)} is NOT perfect.')
