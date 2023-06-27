from collections import deque


def solution(n, m, pos_list):
    queue = deque([str(x) for x in range(1, n + 1)])
    pos_list = deque(pos_list)

    answer = 0
    while pos_list:
        if queue[0] == pos_list[0]:
            pos_list.popleft()
            queue.popleft()
            continue

        new_pos = queue.index(pos_list[0]) + 1
        if new_pos <= len(queue) // 2 + 1:
            diff = 1 - new_pos
            queue.rotate(diff)
            answer += abs(diff)
        else:
            diff = len(queue) - new_pos + 1
            queue.rotate(diff)
            answer += diff
        

    print(answer)

    
if __name__ == "__main__":
    # 입력
    N, M = list(map(int, input().split()))
    pos_list = list(input().split())

    solution(N, M, pos_list)
    