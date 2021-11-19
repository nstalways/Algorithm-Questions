N = input()

N = int(N)

cnt = 0
basis = 1
num_room = 1

if 1 <= N <= 1000000000:
    while True:
       basis = basis + 6 * cnt
       cnt += 1

       if N <= basis:
           print(cnt)
           exit()

else:
    print('N은 1 이상 10억 이하의 자연수입니다.')