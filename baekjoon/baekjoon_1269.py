from sys import stdin

# 입력부
num_a, num_b = map(int, stdin.readline().strip().split())
A = set(map(int, stdin.readline().strip().split()))
B = set(map(int, stdin.readline().strip().split()))

# 문제
print(len(A - B) + len(B - A))