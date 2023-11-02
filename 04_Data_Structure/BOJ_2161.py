from collections import deque

# 입력
N = int(input())
cards = [i for i in range(1, N + 1)]

# 풀이
cards = deque(cards)

ans = []
while len(cards) > 1:
    ans.append(cards.popleft()) # 버리기
    cards.append(cards.popleft()) # 최상단 카드를 맨 아래로 옮기기

print(*ans, *cards)
