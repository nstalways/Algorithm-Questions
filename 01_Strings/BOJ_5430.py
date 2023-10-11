import sys
from collections import deque

def solution(p, n, arr):
    if arr[0] == '':
        arr = []

    arr = deque(arr)    
    direction = 0 # 0: forward, 1: backward
    for op in p:
        if op == 'R':
            direction = not direction

        else:
            if direction == 0: # forward
                try:
                    arr.popleft()
                except:
                    return 'error'

            else: # backward
                try:
                    arr.pop()
                except:
                    return 'error'
    
    if not arr:
        return '[]'
    
    arr = list(arr)
    if direction == 1:
        arr = arr[::-1]

    arr[0] = '[' + arr[0]
    arr[-1] = arr[-1] + ']'

    return ','.join(arr)


if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input().strip())
    ans = []
    for _ in range(T):
        p = input().strip()
        n = int(input().strip())
        arr = input().strip()[1:-1].split(',')

        ans.append(solution(p, n, arr))

    print(*ans, sep='\n')
