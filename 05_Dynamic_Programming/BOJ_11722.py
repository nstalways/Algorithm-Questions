import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
arr = [0] + list(map(int, input().split()))

# 풀이
dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    flag = True
    for j in range(i - 1, -1, -1):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            flag = False 
    
    if flag:
        dp[i] = 1

print(max(dp))
