import sys
input = sys.stdin.readline

# 입력
n = int(input().strip())
m = int(input().strip())

relations = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())

    relations[a].append(b)
    relations[b].append(a)

# 풀이
from collections import deque

visited = [False] * (n + 1)

visited[1] = True
queue = deque([(1, 1)])

ans = 0
while queue:
    my_id, depth = queue.popleft()

    if depth >= 3:
        continue

    for freind_id in relations[my_id]:
        if not visited[freind_id]:
            visited[freind_id] = True
            queue.append((freind_id, depth + 1))

            ans += 1

print(ans)
