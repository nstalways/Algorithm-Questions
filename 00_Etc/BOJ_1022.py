def solution(r, c):
    base_idx = max(abs(r), abs(c))

    rb1 = (2 * (base_idx - 1) + 1) ** 2
    rb2 = (2 * base_idx + 1) ** 2

    dr = base_idx - r
    dc = base_idx - c

    if r >= c:
        return rb2 - dr - dc
    else:
        return rb1 + dc + dr

if __name__ == "__main__":
    r1, c1, r2, c2 = map(int, input().split())

    arr = []
    max_num = 0

    for r in range(r1, r2 + 1):
        tmp = []
        for c in range(c1, c2 + 1):
            num = solution(r, c)
            max_num = max(max_num, num)

            tmp.append(num)

        arr.append(tmp)

    max_len = len(str(max_num))
    
    for row in arr:
        tmp = []
        for num in row:
            tmp.append(str(num).rjust(max_len))

        print(' '.join(tmp))
