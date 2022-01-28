N = int(input())

sys_param = {'iter':10000001}

# update_param
cnt = 1
denom = 0 # 분모
numer = 0 # 분자
prev_num = 1
new_num = 1

if 1<= N <= 10000000:
    for i in range(sys_param['iter']):       
        if prev_num <= N <= new_num:
            break

        prev_num = new_num + 1
        new_num += (i + 2)
        cnt += 1

    if (cnt % 2) == 0: # 짝수일 때
        denom = cnt - (N - prev_num)
        numer = 1 + (N - prev_num)  
    else: # 홀수일 때
        denom = cnt - (new_num - N)
        numer = 1 + (new_num - N)
    
    print(f'{numer}/{denom}')
else:
    print('X는 1 이상 천만 이하의 자연수입니다.')