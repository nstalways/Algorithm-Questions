import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
M = int(input().strip())

broken_buttons = set()
if M: broken_buttons = set(input().split())

# 풀이: 완전탐색
# N과 가장 가까운 숫자 찾기
buttons = set([str(i) for i in range(10)])
can_use = buttons - broken_buttons

start = 100
stack = []
def dfs(limit):
    # 갱신 조건
    if len(stack) == limit:
        global start

        candidate = int(''.join(stack))
        if abs(N - candidate) < abs(N - start):
            start = candidate

        return
    

    for button in can_use:
        stack.append(button)
        dfs(limit)
        stack.pop()


for i in [-1, 0, 1]:
    lim = len(str(N)) + i
    if lim > 0:
        dfs(limit=lim)

# 눌러야하는 횟수 구하기
n_push = min(abs(N - 100), len(str(start)) + abs(N - start))
print(n_push)
