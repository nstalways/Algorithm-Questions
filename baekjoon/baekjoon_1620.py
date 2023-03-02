from sys import stdin

N, M = map(int, stdin.readline().strip().split())

# 입력부
poketmons_num_first, poketmons_name_first = {}, {}
for num in range(1, N+1):
    poketmon = stdin.readline().strip()
    poketmons_num_first[str(num)] = poketmon
    poketmons_name_first[poketmon] = str(num)

# 문제
problems = [stdin.readline().strip() for _ in range(M)]
for prob in problems:
    try:
        tmp = int(prob)     # int 변환이 가능하다면 포켓몬의 번호가 주어진 것
        print(poketmons_num_first[prob])
    except:
        print(poketmons_name_first[prob])   # 예외처리가 됐다면 포켓몬의 이름이 주어진 것
    