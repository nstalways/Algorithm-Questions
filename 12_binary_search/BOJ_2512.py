import sys

# 이분 탐색
def solution(N, data, M):
    if sum(data) <= M:
        print(max(data))
        return

    lb, ub = 1, M

    while True:
        if lb > ub:
            tmp = max(data)
            if tmp >= ub:
                print(ub)
            else:
                print(tmp)
                
            break

        setting = (lb + ub) // 2

        res = 0
        for d in data:
            if d <= setting:
                res += d
            else:
                res += setting
        
        if res <= M:
            lb = setting + 1
        else:
            ub = setting - 1


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    data = list(map(int, input().split()))
    M = int(input().strip())

    solution(N, data, M)
