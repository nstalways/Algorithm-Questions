# 피보나치 수 구하기
# 시간 제한: 1초

import time

def fib_recur(n):
    n0 = 0
    n1 = 1

    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

def fib_recur2(n, n0=0, n1=1):
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return fib_recur2(n-1, n1, n0 + n1)

n = int(input())

if 0 <= n <= 20:
    start = time.time()
    print(fib_recur(n))
    end = time.time()
    print(f'Time with no updating state: {start - end}')

    start2 = time.time()
    print(fib_recur2(n))
    end2 = time.time()
    print(f'Time with updating state: {start2-end2}')

else:
    print('주어진 조건에 맞게 값을 입력해주세요.')