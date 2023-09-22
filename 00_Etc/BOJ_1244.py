import sys

def solution(switch_status, student_info_lst):
    for gender, switch in student_info_lst:
        if gender == 1:
            for i in range(switch, len(switch_status) + 1, switch):
                _, mod = divmod(switch_status[i - 1] + 1, 2)
                switch_status[i - 1] = mod

        elif gender == 2:
            _, mod = divmod(switch_status[switch - 1] + 1, 2)
            switch_status[switch - 1] = mod

            pos1, pos2 = switch - 2, switch

            while True:
                if pos1 < 0 or pos2 >= len(switch_status):
                    break

                switch1_status = switch_status[pos1]
                switch2_status = switch_status[pos2]

                if switch1_status == switch2_status:
                    _, mod = divmod(switch1_status + 1, 2)
                    switch_status[pos1] = mod
                    switch_status[pos2] = mod

                    pos1 -= 1
                    pos2 += 1

                else:
                    break

    for start in range(0, len(switch_status), 20):
        print(' '.join(list(map(str, switch_status[start:start + 20]))))


if __name__ == "__main__":
    num_switch = int(input()) # 1 이상 100 이하
    switch_status = list(map(int, sys.stdin.readline().split()))

    num_students = int(input())
    student_info_lst = []

    for _ in range(num_students):
        student_info_lst.append(list(map(int, input().split())))

    solution(switch_status, student_info_lst)
