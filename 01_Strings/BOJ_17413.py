import sys

# TODO: 좀 더 깔끔하게 풀 수는 없을까...
# 대기업 문자열 코테 문제랑 느낌이 비슷함
def solution(s):
    res = []
    stack = []
    len_s = len(s)
    for i in range(len_s):
        ch = s[i]
        stack.append(ch)

        if stack[0] != '<':
            if stack[-1] == ' ':
                res.append(''.join(stack[:-1][::-1]))
                res.append(stack[-1])

                stack = []
            elif stack[-1] == '<':
                res.append(''.join(stack[:-1][::-1]))
                
                stack = [stack[-1]]

        else:
            if stack[-1] == '>':
                res.append(''.join(stack))

                stack = []

    if stack:
        res.append(''.join(stack[::-1]))

    print(*res, sep='')


if __name__ == "__main__":
    S = sys.stdin.readline().strip()

    solution(S)
