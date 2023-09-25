def solution(n, k):
    members = [i for i in range(1, n + 1)]
    res = []

    pos = k - 1
    while True:
        target = members.pop(pos)
        res.append(str(target))

        if not members:
            break

        pos = (pos + k - 1) % len(members)

    print('<' + ', '.join(res) + '>')
    

if __name__ == "__main__":
    N, K = map(int, input().split())

    solution(N, K)
