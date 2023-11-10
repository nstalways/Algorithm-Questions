# 입력
cost = int(input())

# 풀이
"""
거스름돈 개수가 가장 적게 잔돈을 준다 -> 큰 단위의 돈을 많이 사용한다.
"""
moneys = [500, 100, 50, 10, 5, 1]

changes = 1000 - cost
ans = 0

for money in moneys:
    div, mod = divmod(changes, money)
    ans += div

    changes -= (money * div)

print(ans)
