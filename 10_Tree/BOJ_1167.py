import sys


def solution(tree, start):

    def dfs(start):
        stack = [(start, 0)]
        visited = [False] * (len(tree) + 1)
        visited[start] = True

        farthest_vt = 0
        farthest_dist = 0

        while stack:
            vt, dist = stack.pop()

            if dist > farthest_dist:
                farthest_vt = vt
                farthest_dist = dist

            for next_vt, next_dist in tree[vt]:
                new_dist = dist + next_dist

                if not visited[next_vt]:
                    visited[next_vt] = True
                    stack.append((next_vt, new_dist))
                    
        return farthest_vt, farthest_dist
    
    vt, _ = dfs(1)
    _, answer = dfs(vt)
    
    return answer


if __name__ == "__main__":
    # 입력
    V = int(input())

    tree = {node: [] for node in range(1, V + 1)}

    for _ in range(V):
        vertex_info = list(map(int, sys.stdin.readline().split()))

        vt1 = vertex_info[0]
        for start in range(1, len(vertex_info) - 2, 2):
            vt2, dist = vertex_info[start:start + 2]
            
            tree[vt1].append((vt2, dist))

    print(solution(tree, 1))
    