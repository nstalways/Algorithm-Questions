import sys

# l <= r
def solution(l: str, r: str):
    ans = 0
    
    # padding
    min_len, max_len = len(l), len(r)
    l = '0' * (max_len - min_len) + l

    # 차이 계산
    diff = int(r) - int(l)
    len_diff = len(str(diff))

    # l - r 길이가 2보다 작다
    if len_diff < 2:
        for idx in range(max_len):
            if (l[idx], r[idx]) == ('8', '8'):
                ans += 1
        
        print(ans)
        
    # 2 이상이면
    else:
        idx_to_check = [i for i in range(max_len - len_diff)]
        for idx in idx_to_check:
            if (l[idx], r[idx]) == ('8', '8'):
                ans += 1
        
        print(ans)

def solution2(l, r):
    ans = 0

    # padding
    min_len, max_len = len(l), len(r)
    l = '0' * (max_len - min_len) + l

    for idx in range(max_len):
        if l[idx] == r[idx]:
            if l[idx] == '8':
                ans += 1
        else:
            break
    
    print(ans)


if __name__ == "__main__":
    L, R = sys.stdin.readline().split()

    solution(L, R)
    solution2(L, R)
