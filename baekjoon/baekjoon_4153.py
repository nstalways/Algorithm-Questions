# 주어진 세 변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
# 입력: 30,000 보다 작은 양의 정수로 주어지고, 각 변의 길이를 의미함.
# 출력: 각 입력에 대해 직각삼각형이 맞다면 'right', 아니라면 'wrong'을 출력.
# 시간 제한: 1초

data = []
flag = True

while flag:
    data.append(list(map(int, input().split())))

    if [0, 0, 0] == data[-1]:
        flag = False

for val in data:
    c = val.pop(val.index(max(val)))
    
    a, b = val[0], val[1]

    if (a==0) and (b==0) and (c==0):
        break

    if (0 <= a <= 3*10**(4)) and (0 <= b <= 3*10**(4)) and (0 <= c <= 3*10**(4)):
        if (a**2 + b**2) == (c**2):
            print('right')
        else:
            print('wrong')