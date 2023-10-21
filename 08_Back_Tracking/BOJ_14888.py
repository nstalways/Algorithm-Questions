import sys

def solution(N, A_lst, op_lst):
    """
    1. 식의 계산은 무조건 앞에서부터
    2. 나눗셈은 정수 나눗셈으로, 몫만 취함
    3. 음수를 양수로 나눌 때에는, 음수를 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼다.

    goal) 계산 결과의 최대, 최소를 순서대로 출력
    """
    ans = [float('-inf'), float('inf')] # 최대, 최소

    # TODO: 갱신 함수
    def update(res):
        max_val, min_val = ans
        ans[0] = max(max_val, res)
        ans[1] = min(min_val, res)

    # TODO: 식 계산 함수
    def calculate(op_sequence):
        res = A_lst[0]
        for i in range(1, N):
            op = op_sequence[i - 1]
            num = A_lst[i]

            if op == 'add':
                res += num
            elif op == 'sub':
                res -= num
            elif op == 'mul':
                res *= num
            elif op == 'div':
                if res < 0:
                    res = -(-res // num)
                else:
                    res //= num
        
        update(res)

    # TODO: 연산자 끼워넣는 함수
    cnt = [0, 0, 0, 0] # 덧셈, 뺄셈, 곱셈, 나눗셈 개수
    op_table = {0: 'add', 1: 'sub', 2: 'mul', 3: 'div'}
    op_sequence = []
    def mk_equation():
        if cnt == op_lst:
            calculate(op_sequence)
            return
        
        for select in range(4):
            if cnt[select] < op_lst[select]:
                cnt[select] += 1
                op_sequence.append(op_table[select])

                mk_equation()

                cnt[select] -= 1
                op_sequence.pop()

    mk_equation()
    print(*ans, sep='\n')


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip()) # 수의 개수
    A_lst= list(map(int, input().split())) # 수열 (순서 고정)
    op_lst = list(map(int, input().split())) # 연산자 개수

    solution(N, A_lst, op_lst)
