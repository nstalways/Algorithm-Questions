# 각 층에 W 개의 방이 있음
# 총 H 개의 층이 있음 (총 방의 개수: H x W)
# 정문에서 엘리베이터까지의 거리는 무시
# 모든 인접한 두 방 사이의 거리는 같은 거리, 호텔의 정면 쪽에만 방이 있다고 가정
# 방 번호 format: (YXX), (YYXX) / Y: 층 수, XX: 엘리베이터에서 세었을 때의 번호.
# 손님은 엘리베이터를 타고 이동하는 거리는 신경쓰지 않음. 단, 걷는 거리가 같을 때는 아래층의 방을 더 선호함. ex) 선호도: 102호 < 301호
# 초기에 모든 방이 비어있음.
# GOAL: N 번째로 도착한 손님에게 배정될 방 번호를 계산해야 함.
# 입력) T: 테스트 데이터의 개수, 각 테스트 데이터는 한 행으로서 H(호텔의 층 수), W(각 층의 방 수), N(몇 번째 손님)
# 1 <= H, W <= 99 / 1 <= N <= H x W
# 시간 제한 = 1초

import math

# 테스트 데이터의 개수
T = int(input())

# 호텔 정보, 손님 번호
info = []

for _ in range(T):
    info.append(input())

# 알고리즘
for x in info:
    hwn = x.split()
    H = int(hwn[0]) # 호텔의 층 수
    W = int(hwn[1]) # 호텔의 방 수
    N = int(hwn[2]) # 손님 번호

    # 기본 조건 확인
    if (1 <= H <= 99) and (1 <= W <= 99) and (1 <= N <= (H*N)):
        # 손님의 번호가 몇 층, 몇 번째 방에 속하는 지 확인
        last_num = math.ceil(N / H) # ex) (H, W, N) = (6, 8, 16) / last_num = 3
        floor = int(N % H) # floor = 4

        # 방 번호 만들기 (YXX) or (YYXX)
        if len(str(last_num)) < 2: # 한 자릿수
            last_num = '0' + str(last_num)
        if floor == 0:
            floor = H
        
        room_num = str(floor) + str(last_num)
        print(room_num)

    else:
        print('기본 조건에 맞게 값을 입력해주십시오.')
        break
