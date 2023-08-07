import sys
from collections import defaultdict


# DFS
def solution(graph, start=0):
    visited = [start]
    stack = [(0, start)] # (상대 거리, 시작 지점)

    answer = 0
    while stack:
        rel_dist, curr_node = stack.pop()
        
        if rel_dist < 2:
            for next_node in graph[curr_node]:
                if next_node not in visited:
                    stack.append((rel_dist + 1, next_node))
                    visited.append(next_node)
                    answer += 1
        else:
            continue
        
    return answer


if __name__ == "__main__":
    N = int(input())

    graph = defaultdict(int)
    for name in range(N):
        graph[name] = [idx for idx, check in enumerate(sys.stdin.readline().strip()) if check == "Y"]

    answer = float('-inf')
    for name in range(N):
        answer = max(answer, solution(graph, name))

    print(answer)
    