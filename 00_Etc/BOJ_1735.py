# 입력
n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

# 풀이
"""
1. d1과 d2의 최소공배수 d3를 찾는다.
2. n1에 d3 // d1, n2에 d3 // d2를 곱한 값으로 n1, n2를 갱신한다.
3. n1과 n2를 더해 n3를 만든다.
4. n3와 d3의 최대공약수를 찾는다.
5. 최대공약수로 n3와 d3를 나누어, 기약분수의 분자와 분모를 얻는다.
"""
import math

# 1
d3 = math.lcm(d1, d2)

# 2
n1 *= (d3 // d1)
n2 *= (d3 // d2)

# 3
n3 = n1 + n2

# 4
gcd = math.gcd(n3, d3)

# 5
print(n3 // gcd, d3 // gcd)
