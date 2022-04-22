import math

radius = int(input())

if 1 <= radius <= 10**4:
    print('{:.6f}'.format(math.pi*radius**2))
    print('{:.6f}'.format(2*radius**2))
else:
    print('반지름 R은 10,000보다 작거나 같은 자연수입니다.')