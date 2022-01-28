from math import ceil, floor


sys_param = {'max_range':1000000000}

param = input()
A, B, V = param.split()
A = int(A)
B = int(B)
V = int(V)

if 1 <= B < A <= V <= sys_param['max_range']:
    day = ceil((V - B) / (A - B))
    print(day)
else:
    print('입력은 주어진 조건을 만족해야 합니다.')

# print(f'A: {A}')
# print(f'B: {B}')
# print(f'V: {V}')