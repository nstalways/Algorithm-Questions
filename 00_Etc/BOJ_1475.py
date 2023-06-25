# 구현
from collections import Counter


def solution(n):
    num_set = {str(x):1 for x in range(10)}
    
    answer = 1
    for ch in list(n):
        if num_set[ch] == 0:
            if ch == '6' and num_set['9'] > 0:
                num_set['9'] -= 1
                continue
            elif ch == '9' and num_set['6'] > 0:
                num_set['6'] -= 1
                continue
            
            num_set[ch] -= 1
            num_set = {key:value+1 for key, value in num_set.items()}
            answer += 1
            continue

        num_set[ch] -= 1

    print(answer)


if __name__ == "__main__":
    N = input()

    solution(N)
