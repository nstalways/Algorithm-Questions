import sys
sys.setrecursionlimit(10**6)

# 입력
A, B, C = map(int, input().split())

# 풀이
"""
그래프 탐색: DFS
- C부터 탐색을 수행
- 탐색 과정에서 물통에 들어있는 물의 양을 기록
- 기록한 물의 양을 확인했을 때, A가 비어있다면 정답에 기록
- 기록한 물의 양을 확인했을 때, 이미 탐색했었던 물의 양이라면 탐색을 종료
"""
ans = set()
mem = []

def dfs(water = [0, 0, C]):
    # 종료 조건
    if water in mem:
        return
    else:
        mem.append(water)

    # 기록
    if water[0] == 0:
        ans.add(water[-1])  

    # 탐색
    if water[0]:
        # A -> B
        tmp = water[1] + water[0]
        if tmp <= B:
            b, a = tmp, 0
        else:
            b, a = B, tmp - B
        
        dfs([a, b, water[2]])

        # A -> C
        tmp = water[2] + water[0]
        if tmp <= C:
            c, a = tmp, 0
        else:
            c, a = C, tmp - C

        dfs([a, water[1], c])

    if water[1]:
        # B -> A
        tmp = water[0] + water[1]
        if tmp <= A:
            a, b = tmp, 0
        else:
            a, b = A, tmp - A
        
        dfs([a, b, water[2]])

        # B -> C
        tmp = water[2] + water[1]
        if tmp <= C:
            c, b = tmp, 0
        else:
            c, b = C, tmp - C

        dfs([water[0], b, c])

    if water[2]:
        # C -> A
        tmp = water[0] + water[2]
        if tmp <= A:
            a, c = tmp, 0
        else:
            a, c = A, tmp - A
        
        dfs([a, water[1], c])

        # C -> B
        tmp = water[1] + water[2]
        if tmp <= B:
            b, c = tmp, 0
        else:
            b, c = B, tmp - B

        dfs([water[0], b, c])

dfs()

# 정답 출력
ans = list(ans)
ans.sort()
print(*ans)
