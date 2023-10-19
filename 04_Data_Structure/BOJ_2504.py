import sys

# 분배 법칙
def solution(string):
    stack = []
    
    res, tmp = 0, 1
    for i, ch in enumerate(string):
        if ch == '(':
            stack.append(ch)
            tmp *= 2
            
        elif ch == '[':
            stack.append(ch)
            tmp *= 3

        elif ch == ')':
            if stack and stack[-1] == '(':
                if string[i - 1] == '(':
                    res += tmp

                stack.pop()
                tmp //= 2
            else:
                res = 0
                break

        elif ch == ']':
            if stack and stack[-1] == '[':
                if string[i - 1] == '[':
                    res += tmp

                stack.pop()
                tmp //= 3
            else:
                res = 0
                break
            
    if stack:
        print(0)
    else:
        print(res)


if __name__ == "__main__":
    string = sys.stdin.readline().strip()

    solution(string)
