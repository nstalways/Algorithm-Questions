# 입력
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 풀이
"""
>> 배열 * M을 통해, 같은 수를 여러 번 뽑을 수 있도록 arr 구성
>> 이후 순열과 set을 이용하여 가능한 경우의 수를 찾고, 오름차순 정렬 후 출력

* 위 풀이는 시간 초과가 발생해서, dfs + backtracking으로 접근
>> arr를 오름차순 정렬
>> 이후 dfs + backtracking을 수행
>> 만약 stack의 길이가 M과 같다면, 출력
"""
arr.sort()
stack = []

def dfs():
    if len(stack) == M:
        print(*stack)
        return

    for i in range(N):
        stack.append(arr[i])
        dfs()
        stack.pop()

dfs()
