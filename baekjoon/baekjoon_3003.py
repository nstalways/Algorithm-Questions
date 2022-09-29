# 체스는 총 16개의 피스로 구성됨
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성
# 흰색 피스의 개수가 주어졌을 때, 몇 개를 더허거나 빼야 올바른 세트가 되는지 구하는 프로그램 작성
# 피스의 개수는 0 이상 10 이하인 정수

piece = [1, 1, 2, 2, 2, 8]

data = list(map(int, input().split()))
# print(data)

white_piece = [piece[idx] - data[idx] for idx in range(len(piece))]

for m in white_piece:
    print(m, end=' ')