# 입력
n, m = map(int, input().split())

# 풀이
"""
divmod 사용
"""
div, mod = divmod(n, m)
print(div)
print(mod)
