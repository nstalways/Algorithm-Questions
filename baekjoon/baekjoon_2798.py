from itertools import combinations
from tkinter import Y

condition = list(map(int, input().split()))
N, M = condition[0], condition[1]

numbers = list(map(int, input().split()))
# print(numbers)

def combination(data, num):
    return list(combinations(data, num))

# 메인 알고리즘
best_val = 0
combination_list = combination(numbers, 3)

for comb in combination_list:
    curr_val = sum(comb)

    if best_val < curr_val <= M:
        best_val = curr_val

print(best_val)