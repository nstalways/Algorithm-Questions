import sys
import time

def solution(K, N, infos):
    min_val, max_val = 1, max(infos)

    while True:
        if max_val < min_val:
            print(max_val)
            break

        length = (min_val + max_val) // 2

        cnt = 0
        for info in infos:
            cnt += (info // length)

        if cnt < N:
            max_val = length - 1
        else:
            min_val = length + 1


if __name__ == "__main__":
    input = sys.stdin.readline

    K, N = map(int, input().split())
    
    infos = []
    for _ in range(K):
        infos.append(int(input().strip()))

    solution(K, N, infos)
