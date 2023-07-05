# 과거의 내가 풀었던 방법을 보고 공부해서 다시 푼 문제..

def solution(x):
    # params
    cnt = 1
    numer, denom = 0, 0
    start, end = 1, 1

    # x가 몇 번쨰 대각선에 속해있는지 체크
    for i in range(10**7 + 1):
        if (start <= x) and (x <= end):
            break

        start = end + 1
        end += (i + 2)
        cnt += 1 # 대각선 시작 방향 확인용

    if (cnt % 2) == 0: # cnt가 짝수일 경우 아래 방향
        numer = 1 + (x - start)
        denom = 1 + (end - x)
    else: # cnt가 홀수일 경우 윗 방향
        numer = 1 + (end - x)
        denom = 1 + (x - start)
    
    print(f'{numer}/{denom}')


if __name__ == "__main__":
    # 입력
    X = int(input()) # X 번째 분수

    solution(X)