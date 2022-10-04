N = int(input())
divisor = list(map(int, input().split()))

if len(divisor) == 1:
    print(divisor[0]**2)
else:
    print(max(divisor) * min(divisor))