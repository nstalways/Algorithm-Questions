import sys

# 입력
N = list(sys.stdin.readline().strip())

# 풀이
N.sort(reverse=True)

if N[-1] != '0':
    print(-1)
else:
    res = int(''.join(N))

    if (res % 30) != 0:
        print(-1)
    else:
        print(res)
        