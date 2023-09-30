import sys

def solution(members: dict):
    ans = []
    for ch, cnt in members.items():
        if cnt >= 5:
            ans.append(ch)
    
    if ans:
        ans.sort()
        print(''.join(ans))
    else:
        print('PREDAJA')


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    members = {}
    for _ in range(N):
        first_name = input().strip()
        first_ch = first_name[0]

        if first_ch in members.keys():
            members[first_ch] += 1
        else:
            members[first_ch] = 1

    solution(members)
