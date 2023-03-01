from sys import stdin

N, M = map(int, stdin.readline().strip().split())

# 입력부
set_s, strings = [], []
for _ in range(N):
    set_s.append(stdin.readline().strip())

for _ in range(M):
    strings.append(stdin.readline().strip())

cnt = 0
for s in strings:
    if s in set_s:
        cnt += 1

print(cnt)