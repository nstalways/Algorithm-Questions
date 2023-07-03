def solution(start, end, graph, visited):
    stack = [start]
    visited[start] += 1

    while stack:
        curr = stack.pop()

        for next in graph[curr]:
            if not visited[next]:
                stack.append(next)
                visited[next] = visited[curr] + 1               
    
    if visited[end]:
        print(visited[end] - 1)
    else:
        print('-1')


if __name__ == "__main__":
    # 입력
    n = int(input())
    target_a, target_b = map(int, input().split())
    m = int(input())

    bi_dir_graph = [[] for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        bi_dir_graph[x].append(y)
        bi_dir_graph[y].append(x)
    
    solution(target_a, target_b, bi_dir_graph, visited)
