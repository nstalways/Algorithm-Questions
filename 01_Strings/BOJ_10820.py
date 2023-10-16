import sys

def solution(s):
    lower, upper = 0, 0
    digit, empty = 0, 0

    for ch in s:
        if ch.isalpha():
            if ch == ch.lower():
                lower += 1
            else:
                upper += 1

        elif ch.isdigit():
            digit += 1
        else:
            empty += 1

    return (lower, upper, digit, empty)


if __name__ == "__main__":
    input = sys.stdin.readline

    ans = []
    while True:
        tmp = input().strip('\n')
        if tmp:
            res = solution(tmp)
            ans.append(res)

        else:
            break

    for a in ans:
        print(*a, sep=' ')
