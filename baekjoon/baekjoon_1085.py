# 직사각형에서 탈출
# 현재 위치: (x, y)
# 직사각형의 왼쪽 아래 꼭짓점 (0, 0)
# 오른쪽 위 꼭짓점 (w, h)
# 직사강형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성
# 입력: 첫째 줄에 x, y, w, h가 주어짐
# 출력: 첫째 줄에 문제의 정답을 출력함
# 조건: 1. 1 <= w,h <= 1,000 / 2. 1 <= w <= w-1 / 3. 1 <= y <= h-1 / 4. x, y, w, h는 정수
# 시간 제한: 2초

info = list(map(int, input().split()))

x, y, w, h = info[0], info[1], info[2], info[3]

if (1 <= w <= 10**3) and (1 <= h <= 10**3) and (1 <= x <= w-1) and (1 <= y <= h-1) and (type(x) is int) and (type(y) is int) and (type(w) is int) and (type(h) is int):
    sub_x = w - x
    sub_y = h - y
    
    print(min([x, y, sub_x, sub_y]))

else:
    print('주어진 조건에 맞게 값을 입력해주세요.')