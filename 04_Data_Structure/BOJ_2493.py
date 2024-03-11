import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
towers = list(map(int, input().split()))

# 풀이
"""
goal: 각각의 탑에서 발사한 레이저 신호를 "수신한 탑들의 번호"를 출력 (없으면 0을 출력)
note:
    - 모든 탑의 높이는 다름 (중복 X)
    - 모든 탑은 레이저 송신기를 가지고 있으며, 지표면과 평행하게 "수평 직선의 왼쪽 방향"으로 발사함
    - 하나의 탑에서 발사된 레이저 신호는 "가장 먼저 만나는 단 하나의 탑"에서만 수신이 가능
how:
    - stack 활용
"""
tower2idx = {tower: idx for idx, tower in enumerate(towers)} # 입력 배열에서 탑의 위치
arr = [0] * N # 정답 배열 -> 0으로 초기화
stack = [] # 비교할 탑들을 저장

while towers:
    tower = towers.pop()
    if not tower:
        stack.append((tower, tower2idx[tower])) # (탑 높이, 배열 위치)
        continue

    for i in range(len(stack) - 1, -1, -1):
        if stack and tower > stack[i][0]: # 현재 탑의 높이가 이전 탑보다 높다면
            arr[stack[i][1]] = tower2idx[tower] + 1 # 이전 탑의 위치에 현재 탑의 번호 (위치 + 1) 를 저장하고
            stack.pop() # 이전 탑은 제거
            
        else:
            break

    stack.append((tower, tower2idx[tower])) # 현재 탑 정보를 추가

print(*arr)
