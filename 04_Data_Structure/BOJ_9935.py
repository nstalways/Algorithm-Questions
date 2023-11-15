import sys
input = sys.stdin.readline

# 입력
s = input().strip()
target = list(input().strip())

# 풀이
"""
1. replace() 함수를 활용한 풀이 >> 시간 초과 발생
2. stack을 이용한 풀이
"""
len_target = len(target)

stack = []
for ch in s:
    stack.append(ch)

    if len(stack) >= len_target:
        is_matched = True
        idx = -1
        for i in range(len_target - 1, -1, -1):
            if stack[idx] != target[i]:
                is_matched = False
                break

            idx -= 1

        if is_matched:
            for _ in range(len_target):
                stack.pop()

if not stack:
    print('FRULA')                
else:
    print(''.join(stack))
    