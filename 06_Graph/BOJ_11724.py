import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())

# 풀이
"""
간선의 개수가 많은 편이라 인접 행렬을 쓸까도 했지만, 인접 리스트로 구현하는 것이 좋을 듯
>> 정점 방문 여부를 기록할 배열을 만들고, 해당 정점을 방문하지 않았다면 dfs 탐색을 수행
"""
# 인접 리스트 생성
undirected_graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    undirected_graph[a].append(b)
    undirected_graph[b].append(a)

# 정점 방문 여부 기록
visited = [False] * (N + 1)

# dfs 구현
sys.setrecursionlimit(10**6) # RecursionError 방지

def dfs(_node):
    for next_node in undirected_graph[_node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)    

# 방문하지 않은 정점에 대해 dfs 탐색 수행
ans = 0
for node in range(1, N + 1):
    if not visited[node]:
        ans += 1
        dfs(node)

print(ans)
