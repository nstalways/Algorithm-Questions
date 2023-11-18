# 입력
burger_lst = [int(input()) for _ in range(3)]
drink_lst = [int(input()) for _ in range(2)]

# 풀이
"""
가장 저렴한 버거 + 가장 저렴한 음료 - 50
"""
print(min(burger_lst) + min(drink_lst) - 50)
