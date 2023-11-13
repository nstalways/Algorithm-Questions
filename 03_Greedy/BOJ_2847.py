# 입력
N = int(input())
scores = [int(input()) for _ in range(N)]

# 풀이
ans = 0
for i in range(N - 1, 0, -1):
    if scores[i - 1] >= scores[i]:
        diff = scores[i] - scores[i - 1] - 1
        
        scores[i - 1] += diff
        ans += abs(diff)

print(ans)
