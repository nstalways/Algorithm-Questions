# 수 정렬하기
# 시간 제한: 1초
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 수의 개수 N(1 <= N <= 1,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1000보다 작거나 같은 정수이다.
# 수는 중복되지 않는다.

N = int(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))

# bubble sort
# buble sort의 핵심
# 오름차순으로 정렬 시 인접한 두 element끼리 비교하여 swap하고,
# 맨 마지막 element는 가장 큰 수이므로 제거한다.
result = []

while True:
    length = len(num_list)

    for i in range(length-1):
        flag = num_list[i] > num_list[i+1]
        if flag:
            tmp = num_list[i+1]
            num_list[i+1] = num_list[i]
            num_list[i] = tmp
    
    result.append(num_list.pop())

    if len(result) == N:
        for x in result[-1::-1]:
            print(x)
        break