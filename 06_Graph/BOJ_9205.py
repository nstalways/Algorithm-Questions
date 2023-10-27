import sys
from collections import deque

def solution(n, infos):
    home, festival = infos[0], infos[-1]
    home_else = infos[1:]

    visited = [False] * (n + 1)

    def bfs():
        queue = deque([home])

        flag = False
        while queue:
            x, y = queue.popleft()

            if (x, y) == festival:
                flag = True
                break

            for i, crds in enumerate(home_else):
                if visited[i]:
                    continue

                distance = abs(x - crds[0]) + abs(y - crds[1])

                if (distance / 50) <= 20:
                    queue.append(crds)
                    visited[i] = True

        return 'happy' if flag else 'sad'
    
    return bfs()

if __name__ == "__main__":
    input = sys.stdin.readline

    ans = []
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        
        infos = []
        for _ in range(n + 2):
            infos.append(tuple(map(int, input().split())))

        ans.append(solution(n, infos))
    
    print(*ans, sep='\n')
    