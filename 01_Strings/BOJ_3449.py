import sys
import time

# 단순 반복
def solution(test_case):
    start = time.time()
    for bnum1, bnum2 in test_case:
        len_bnum = len(bnum1)
        cnt = 0
        for idx in range(len_bnum):
            if bnum1[idx] != bnum2[idx]:
                cnt += 1

        print(f'Hamming distance is {cnt}.')
    
    print(f'{time.time() - start:.4f}')

# 비트 마스킹(T가 커질수록, 문자열의 길이가 길어질수록 효율적)
def solution2(test_case):
    start = time.time()
    for bnum1, bnum2 in test_case:
        bnum1 = int(bnum1, 2)
        bnum2 = int(bnum2, 2)

        xor_result = bnum1 ^ bnum2

        dist = 0
        while xor_result:
            dist += xor_result & 1
            xor_result >>= 1
        
        print(f'Hamming distance is {dist}.')

    print(f'{time.time() - start:.4f}')


if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input().strip())
    test_case = []
    for _ in range(T):
        test_case.append(tuple([input().strip() for _ in range(2)]))
    
    solution(test_case)
    solution2(test_case)
