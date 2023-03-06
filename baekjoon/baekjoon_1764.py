from sys import stdin

# 입력부
N, M = map(int, stdin.readline().strip().split())

deutdo, bodo = [], []
for _ in range(N):
    deutdo.append(stdin.readline().strip())

for _ in range(M):
    bodo.append(stdin.readline().strip())

deutdo, bodo = set(deutdo), set(bodo)

# 문제
intersection = list(deutdo & bodo)
intersection.sort()
print(len(intersection))
for i in intersection:
    print(i)
