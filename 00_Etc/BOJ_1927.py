import sys
import heapq


def solution(x_list):
    heap = []

    for x in x_list:
        if x == 0:
            if not heap:
                print(0)
                continue

            print(heapq.heappop(heap))
            continue
            
        heapq.heappush(heap, x)      


if __name__ == "__main__":
    N = int(input())
    
    x_list = []
    for _ in range(N):
        x_list.append(int(sys.stdin.readline()))
    
    solution(x_list)
    