import sys
from collections import deque

def solution(n, p, q):
    if n == 0:
        return 1
    
    # TODO: n을 최소 단위로 쪼개기
    dp = set()
    queue = deque([(n, n // p, n // q)])
    while queue:
        i, i_p, i_q = queue.popleft()
        dp.add((i, i_p, i_q))

        if (i_p, i_q) == (0, 0):
            continue
        
        queue.append((i_p, i_p // p, i_p // q))
        queue.append((i_q, i_q // p, i_q // q))

        queue = deque(set(queue))

    dp = deque(sorted(list(dp), key=lambda x: x[0]))

    # TODO: 최소 단위부터 더해서 A_N 구하기
    a_i_dict = {0: 1}
    while dp:
        i, i_p, i_q = dp.popleft()
        if i == 0:
            continue
        
        a_i_dict[i] = a_i_dict[i_p] + a_i_dict[i_q]
    
    return a_i_dict[n]

if __name__ == "__main__":
    N, P, Q = map(int, sys.stdin.readline().split())

    print(solution(N, P, Q))
