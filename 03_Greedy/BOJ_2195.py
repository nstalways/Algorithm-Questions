import sys

def solution(orig, goal):
    # 1. goal의 첫 문자부터 범위를 확장시키면서, orig와 matching되는 패턴을 찾는다.
    ans = 0
    offset = 1
    while goal:
        part = goal[:offset]
        is_matched = orig.find(part)

        # 1-1. 매칭이 된다면, 범위를 더 늘려본다.
        if is_matched > -1:
            if offset == len(goal):
                ans += 1
                break

            offset += 1

        # 1-2. 매칭이 안되면, 이전 범위의 부분 문자로 goal을 변경하고, 변경된 횟수를 센다.
        else:
            offset -= 1
            goal = goal[offset:]
            ans += 1

            offset = 1
            
    print(ans)


if __name__ == "__main__":
    input = sys.stdin.readline

    S = input().strip()
    P = input().strip()

    solution(S, P)
