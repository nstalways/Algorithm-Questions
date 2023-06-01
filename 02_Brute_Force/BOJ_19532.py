import math


def solution():
    a, b, e, c, d, f = list(map(int, input().split()))

    # 역행렬 사용
    divisor = 1 / (a*d - b*c)
    a, b, c, d = divisor * d, -1 * divisor * b, -1 * divisor * c, divisor * a
    
    x, y = round(a*e + b*f), round(c*e + d*f)
    print(x, y)


if __name__ == "__main__":
    solution()