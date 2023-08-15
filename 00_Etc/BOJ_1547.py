def solution(xy_lst):
    cups = [1, 2, 3]

    for x, y in xy_lst:
        pos_x = cups.index(x)
        pos_y = cups.index(y)

        cups[pos_x] = y
        cups[pos_y] = x

    print(cups[0])


if __name__ == "__main__":
    M = int(input()) # 1 <=, <= 50
    
    xy_lst = []
    for _ in range(M):
        xy_lst.append(tuple(map(int, input().split())))

    solution(xy_lst)
    