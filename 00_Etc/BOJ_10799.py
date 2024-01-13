import sys
input = sys.stdin.readline

# 입력
data = input().strip()

# 풀이
"""
구현 아이디어를 떠올리는 것이 어려웠던 문제
- 쇠막대기와 레이저를 구분하기 위해 '()'를 '*'로 replace
- 열린 괄호는 stack에 누적 (열린 괄호 == 쇠막대기)
- '*'를 만나는 순간 stack에 누적된 열린 괄호의 개수를 정답에 누적
- ')'를 만나는 순간 stack.pop() + 막대의 끝을 의미하므로 정답에 1 추가
"""
data = data.replace('()', '*')

ans = 0
stack = []

for ch in data:
    if ch == '(':
        stack.append(ch)

    elif ch == ')':
        stack.pop()
        ans += 1

    elif ch == '*':
        ans += len(stack)

print(ans)
