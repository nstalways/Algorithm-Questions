# 이항 계수
# n! / (n-k)! * k!

tmp = list(map(int, input().split()))
N = tmp[0]
K = tmp[1]

def factorial(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * factorial(n-1)

def binomialCoeff(n, k):
    return factorial(n) // (factorial(n-k) * factorial(k))

print(binomialCoeff(N, K))