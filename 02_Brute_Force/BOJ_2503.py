import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())

infos = []
for _ in range(N):
    query, s, b = input().split()
    infos.append((tuple(map(int, list(query))), (int(s), int(b))))

# 풀이
"""
질의응답을 통해 얻은 정보를 바탕으로, 정답 가능성이 있는 경우의 수를 세는 문제

브루트포스
- 123부터 987까지 9*8*7 개의 숫자를 탐색
- 민혁이가 물어본 숫자를 정답으로 간주하고, 후보 숫자를 제시했을 때 스트라이크/볼이 같은지 확인
- 민혁이의 모든 물음에 대해 조건을 만족한다면, 정답 가능성이 있음
- 하나라도 만족하지 않는 조건이 있다면, 정답 가능성이 없음

후기
- 브루트포스로 접근하는 것은 떠올릴 수 있으나, 문제 해결의 핵심 아이디어를 떠올리기 힘들었던 문제
"""
cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if (i == j) or (j == k) or (i == k):
                continue
            
            for q, a in infos:
                flag = False
                s, b = 0, 0

                if i == q[0]:
                    s += 1
                elif i in q:
                    b += 1

                if j == q[1]:
                    s += 1
                elif j in q:
                    b += 1

                if k == q[2]:
                    s += 1
                elif k in q:
                    b += 1

                if (s, b) != a:
                    flag = True
                    break
            
            if flag:
                continue
            
            print(i, j, k)
            cnt += 1

print(cnt)
