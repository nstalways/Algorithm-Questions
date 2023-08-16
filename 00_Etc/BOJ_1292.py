def solution(interval: tuple):
    a, b = interval

    num_lst = [1]
    while len(num_lst) <= 1000:
        target = num_lst[-1] + 1
        num_lst.extend([target for _ in range(target)])

    print(sum(num_lst[a-1:b]))


if __name__ == "__main__":
    A, B = map(int, input().split())

    solution((A, B))
    