# 회의실 1개, 진행하려는 회의는 N개
# 1개의 회의실로 진행할 수 있는 최대 회의 개수 찾기

import sys

def solution(meeting_infos, num_meeting):
    meeting_infos.sort(key=lambda x: (x[1], x[0]))

    prev_meeting = meeting_infos[0]
    cnt = 1
    for i in range(1, num_meeting):
        cur_meeting = meeting_infos[i]

        if cur_meeting[0] < prev_meeting[1]:
            continue
        else:
            cnt += 1
            prev_meeting = cur_meeting

    print(cnt)
    

if __name__ == "__main__":
    input = sys.stdin.readline

    # OK
    N = int(input().strip())
    meeting_infos = []
    for _ in range(N):
        meeting_infos.append(list(map(int, input().split())))

    solution(meeting_infos, N)
