import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())

# 풀이
"""
구현
- 빈 리스트를 stack으로 사용
- 입력이 push이면 값을 추가
- 입력이 pop이면 가장 위에 있는 정수를 빼고, 출력. 단 stack이 비어있는 경우 -1을 출력
- 입력이 size이면 정수의 개수를 출력
- 입력이 empty이면, stack이 비어있으면 1, 아니면 0을 출력
- 입력이 top이면 가장 위에 있는 정수를 출력. 단 stack이 비어있는 경우 -1을 출력
"""
ans = []
stack = []
n_elements = 0

for _ in range(N):
    cmd_in = input().split()
    
    if cmd_in[0] == 'pop':
        try:
            ans.append(stack.pop())
            n_elements -= 1
        except:
            ans.append(-1)

    elif cmd_in[0] == 'size':
        ans.append(n_elements)

    elif cmd_in[0] == 'empty':
        ans.append(0) if stack else ans.append(1)
    
    elif cmd_in[0] == 'top':
        ans.append(stack[-1]) if stack else ans.append(-1)

    else:
        stack.append(cmd_in[1])
        n_elements += 1

print(*ans, sep='\n')
