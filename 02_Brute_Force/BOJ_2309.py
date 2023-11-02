from itertools import combinations

# 입력
heights = [int(input()) for _ in range(9)]

# 풀이
def solution1():
    heights.sort()
    candidates = list(combinations([i for i in range(9)], 7))
    for idx_lst in candidates:
        tmp = []
        for idx in idx_lst:
            tmp.append(heights[idx])

        if sum(tmp) == 100:
            print(*tmp, sep='\n')
            break

# 풀이 2
def solution2():
    ans = []
    def recursive_call():
        if len(ans) == 7 and sum(ans) == 100:
            ans.sort()
            print(*ans, sep='\n')
            exit()

        for height in heights:
            if height not in ans:
                ans.append(height)
                recursive_call()
                ans.pop()

    recursive_call()

solution2()