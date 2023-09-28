import sys
from collections import deque

def solution(words):
    words = deque(sorted(words, key=lambda x: len(x)))
    res = []

    while words:
        word = words.popleft()
        
        flag = True
        for etc_word in words:
            is_first = etc_word.find(word) + 1

            if is_first == 1:
                flag = False
                break

        if flag:
            res.append(word)
        
    ans = len(res)
    
    return ans


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    words = []
    for _ in range(N):
        words.append(input().strip())

    print(solution(words))
    