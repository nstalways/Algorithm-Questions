info = input()
A, B, C = info.split(' ')

A = int(A)
B = int(B)
C = int(C)

if (A and B and C) <= 2100000000:
    if (C - B) <= 0:
        print(-1)
    else:
        num_notebook = A // (C - B) # 고정비용 // (책정비용 - 가변비용)
        tmp_val = num_notebook * (C - B) # 판매량 * (책정비용 - 가변비용) = 순수익

        if tmp_val <= A: # 판매비용 <= 고정비용이면 손익분기점 발생 X
            print(num_notebook + 1)
        else: # 판매비용 > 고정비용이면 손익분기점 발생 O
            print(num_notebook)
else:
    print('A, B, C는 21억 이하의 자연수입니다.')