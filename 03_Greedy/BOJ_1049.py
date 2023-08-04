def solution(n, package_price, piece_price):
    min_package_price = min(package_price)
    min_piece_price = min(piece_price)

    cost = 0
    # 1. 패키지가 피스보다 비싼 경우를 check
    if min_package_price >= min_piece_price * 6:
        cost = min_piece_price * n
    
    else: # 2. 패키지와 피스를 같이 활용
        div, mod = divmod(n, 6)
        
        cost = min(min_package_price * (div + 1),\
                   min_package_price * div + min_piece_price * mod)
    
    print(cost)


if __name__ == "__main__":
    N, M = map(int, input().split())

    price_per_brand = []
    for _ in range(M):
        price_per_brand.append(tuple(map(int, input().split())))

    package_price_list, piece_price_list = [], []
    for price in price_per_brand:
        package_price_list.append(price[0])
        piece_price_list.append(price[1])
    
    solution(N, package_price_list, piece_price_list)
    