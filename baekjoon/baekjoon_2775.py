# 조건
# a층의 b호에 살려면 자신의 아래(a-1) 층의 1호부터 b호까지 사람들의 수의
# 합만큼 사람들을 데려와 살아야 함.
# 아파트에 비어있는 집은 없음. 모든 거주민들은 이 계약 조건을
# 지키고 있음.
# 시간 제한: 1초

# 입력
T = int(input())
info = []

for _ in range(T):
    k = int(input())
    n = int(input())
    info.append([k, n])

# 알고리즘
for val in info:
    k = val[0]
    n = val[1]

    people = 0
    tmp_list = []

    if (1 <= k <= 14) and (1 <= n <= 14):
        for i in range(k):
            prev_list = tmp_list.copy()

            for j in range(n):
                if (i + 1) == 1:
                    people += (j + 1)
                    tmp_list.append(people)
                else:
                    tmp_list[j] = sum(prev_list[:(j+1)])

        print(tmp_list[-1])

    else:
        print('k과 n은 1 이상 14 이하의 자연수입니다.')
        break