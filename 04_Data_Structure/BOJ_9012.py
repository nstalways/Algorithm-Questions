import sys
from collections import deque

def solution(test_dataset):
    ans = []
    for test_data in test_dataset:
        open = []
        test_data = deque(list(test_data))
        is_vps = True
        while test_data:
            parenthesis = test_data.popleft()

            if parenthesis == "(":
                open.append(parenthesis)
            elif parenthesis == ")":
                try:
                    open.pop()
                except:
                    is_vps = False
                    break

        if not is_vps:
            ans.append('NO')
            continue

        if open:
            ans.append('NO')
        else:
            ans.append('YES')

    print(*ans, sep='\n')


if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input().strip())
    test_dataset = []
    for _ in range(T):
        test_dataset.append(input().strip())

    solution(test_dataset)
