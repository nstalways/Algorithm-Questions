condition = list(map(int, input().split()))
N, K = condition[0], condition[1]

score_list = list(map(int, input().split()))
print(sorted(score_list, reverse=True)[K-1])

