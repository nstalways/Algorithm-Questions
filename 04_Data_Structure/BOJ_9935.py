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

    if stack[-len_target:] == target:
        del stack[-len_target:]

if not stack:
    print('FRULA')                
else:
    print(''.join(stack))
    