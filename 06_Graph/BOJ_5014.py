import sys
from collections import deque


def solution(num_floors, start, target, up, down):
    visited_floors = [0 for _ in range(num_floors + 1)]
    visited_floors[start] = 1 # 시작 위치를 방문 처리
    queue = deque([(start, 0)]) # 시작 위치, 이동 횟수

    while queue:
        curr_floor, num_moves = queue.popleft()
        # print(f"현재 층은 {curr_floor}층 입니다.")
        # print(f"이동 횟수는 {num_moves} 입니다.")

        # 현재 층이 G층인 경우
        if curr_floor == target:
            print(num_moves)            
            return

        for move in [up, -down]:
            next_floor = curr_floor + move

            # 예외 처리
            if next_floor < 1 or next_floor > num_floors:
                continue

            if visited_floors[next_floor]:
                continue

            visited_floors[next_floor] = 1 # 방문 처리
            queue.append((next_floor, num_moves + 1))

    print('use the stairs')


if __name__ == "__main__":
    F, S, G, U, D = map(int, sys.stdin.readline().split())

    solution(F, S, G, U, D)
    