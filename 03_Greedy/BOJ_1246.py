# 달걀의 개수: N, 고객: M
# M명의 고객 중 i번째 고객은 달걀 하나를 Pi 가격 이하로 살 수 있음.
# 한 고객에게 한 개의 달걀만 팔 수 있음.
# 달걀의 가격이 A라면, Pi >= A인 모든 고객은 달걀을 산다는 것
# 목표: 최대 수익을 올릴 수 있는 달걀의 가장 낮은 가격을 책정하는 것

def solution(n, p_i):
    p_i.sort()

    sales, price = 0, 0
    num_eggs = n
    num_customers = len(p_i)

    for remains in range(num_customers, 0, -1):
        factor = num_eggs if remains >= num_eggs else remains

        tmp_price = p_i[num_customers - remains]
        tmp_sales = tmp_price * factor

        if tmp_sales > sales:
            sales = tmp_sales
            price = tmp_price

    print(price, sales)


if __name__ == "__main__":
    N, M = map(int, input().split())
    p_i = []
    for _ in range(M):
        p_i.append(int(input()))

    solution(N, p_i)
