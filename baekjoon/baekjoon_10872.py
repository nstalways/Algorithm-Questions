def factorial(N):
    if 0 <= N <= 12:
        # base
        if N == 0:
            return 1
        else:
            return N * factorial(N-1)
    else:
        print('주어진 조건에 맞게 값을 입력해주세요.')

N = int(input())

res = factorial(N)

print(res)