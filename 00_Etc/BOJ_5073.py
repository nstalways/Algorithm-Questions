import sys
input = sys.stdin.readline

ans = []
while True:
    tmp = sorted(list(map(int, input().split())), reverse=True)
    if tmp == [0, 0, 0]:
        print(*ans, sep='\n')
        break

    if tmp[0] >= sum(tmp[1:]):
        ans.append('Invalid')
    else:
        a, b, c = tmp
        if (a == b) and (b == c):
            ans.append('Equilateral')
        elif (a != b) and (b != c) and (a != c):
            ans.append('Scalene')
        else:
            ans.append('Isosceles')
