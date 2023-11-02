import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
arr = list(map(int, input().split()))

# 풀이
"""
stack에 저장되는 숫자들은 무조건 내림차순이다 -> 뒤에서부터 하나씩 확인
"""
ans = [0] * N

stack = []
for i, e in enumerate(arr):
    if stack:
        while stack:
            prev_i, prev_e = stack[-1]

            if prev_e >= e:
                break
            else:
                ans[prev_i] = e
                stack.pop()
        
    stack.append((i, e))

# 후처리
for i, _ in stack:
    ans[i] = -1

print(*ans)
