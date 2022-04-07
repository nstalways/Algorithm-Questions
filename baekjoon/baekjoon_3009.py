# 네 번째 점
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# 입력: 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
# 출력: 직사각형의 네 번째 점의 좌표를 출력한다.
# 시간 제한: 1초

data = []
x = []
y = []

for i in range(3):
    data.append(list(map(int, input().split())))

    x.append(data[i][0])
    y.append(data[i][1])

cond1 = [(1 <= i <= 10**3) for i in x]
cond2 = [(1 <= j <= 10**3) for j in y]

if (cond1 and cond2) == [True, True, True]:
    tmp_list = [[min(x), min(y)],
                [min(x), max(y)],
                [max(x), min(y)],
                [max(x), max(y)]]
    
    for tmp_val in tmp_list:
        if tmp_val in data:
            continue
        else:
            print(tmp_val[0], tmp_val[1])
            break
    
else:
    print('주어진 조건에 맞게 값을 입력해주세요.')