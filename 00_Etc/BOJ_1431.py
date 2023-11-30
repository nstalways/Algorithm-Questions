import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
arr = [input().strip() for _ in range(N)]

# 풀이
"""
주어진 조건에 따라 arr를 정렬하는 문제
>> sort() 함수의 key 인자를 이용해서 정렬을 수행
"""
arr.sort(key=lambda x: (len(x), sum([int(ch) for ch in x if ch.isdigit()]), x))
print(*arr, sep='\n')
