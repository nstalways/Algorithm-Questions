import sys
from collections import deque

def solution(data, n):
    data = [(height, info) for height, info in enumerate(data, start=1)]
    data = data[::-1]

    res = deque([data[0][0]])
    for i in range(1, n):
        height, info = data[i]

        if info == 0:
            res.appendleft(height)
            continue

        cnt, pos = 0, 0
        for prev_height in res:
            if prev_height > height:
                cnt += 1

            pos += 1

            if cnt == info:
                res.insert(pos, height)
                break

    ans = ' '.join([str(height) for height in res])
    print(ans)


def solution2(data, n):
    res = [0] * n
    for height, info in enumerate(data, start=1):
        cnt = 0
        for i in range(n):
            if cnt == info and res[i] == 0:
                res[i] = height
                break

            elif res[i] == 0:
                cnt += 1
    
    print(*res)
    

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())

    data = list(map(int, input().split()))
    
    # solution(data, N)
    solution2(data, N)
    