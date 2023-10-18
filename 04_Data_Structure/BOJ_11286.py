import sys
import heapq

def solution(op_infos):
    ans = []
    pq = []
    for op in op_infos:
        if op == 0:
            try:
                ans.append(heapq.heappop(pq)[-1])
            except:
                ans.append(0)
        else:
            heapq.heappush(pq, (abs(op), op))

    print(*ans, sep='\n')


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    op_infos = [int(input().strip()) for _ in range(N)]

    solution(op_infos)
