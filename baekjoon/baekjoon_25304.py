# 시간 제한: 1초
# 구매한 각 물건의 가격과 개수가 주어졌을 때, 그 총합이 영수증의 총합과 같은지 확인하는 프로그램 작성

X = int(input()) # 총 금액
N = int(input()) # 물건 종류의 수

costAndNumber = []

for _ in range(N):
    costAndNumber.append(list(map(int, input().split())))

predict_cost = 0

for i in range(len(costAndNumber)):
    cost, num = costAndNumber[i][0], costAndNumber[i][1]
    predict_cost += cost * num

if predict_cost == X:
    print('Yes')
else:
    print('No')