import sys
input = sys.stdin.readline

# 입력
N, d, k, c = map(int, input().split())
arr = [int(input().strip()) for _ in range(N)]

# 풀이
"""
브루트 포스, 구현, 해쉬 맵, 자료구조, 최적화, 
- 큐 두 개를 이용하여 구현
- 첫 번째 큐는 먹을 접시, 두 번째 큐는 남은 회전 초밥
- 첫 번째 큐에 k개만큼의 접시가 차면, 종류의 가짓수를 확인하여 정답을 갱신 + 이후 첫 번째 큐의 첫 번째 원소를 두 번째 큐의 끝에 추가
- 위 과정을 반복
- 대략적인 시간 복잡도: O(N)

새로운 풀이 (기존 풀이보다 40배 이상 빠르나, 시험 때 사용하기는 힘든 풀이 (디버깅 과정이 오래 걸림))
- 배열의 요소들이 k개 연속되어야 함.
- 길이가 k인 배열의 요소들 중 변경되는 지점은 맨 앞과 맨 뒤임.
- 맨 앞과 맨 뒤를 변경했을 때 가짓수를 센다.
"""
# 스시 종류들을 기록하는 테이블
sushi_table = [0] * (d + 1)

# 초기 초밥의 가짓수 계산
tmp = set()
for i in range(k):
    sushi = arr[i]
    
    tmp.add(sushi)
    sushi_table[sushi] += 1

n_kinds = len(tmp)
if c not in tmp:
    n_kinds += 1
    sushi_table[c] = 1

# 메인 알고리즘
answer = 0
for i in range(N):
    front, rear = arr[i], arr[(i + k) % N]

    # 맨 앞을 제거했을 때, 해당 스시가 없다면 종류를 1 감소
    sushi_table[front] -= 1
    if not sushi_table[front]:
        n_kinds -= 1

    # 맨 뒤에 추가할 종류가 새로운 것이라면 1 증가
    if not sushi_table[rear]:
        n_kinds += 1

    sushi_table[rear] += 1

    # 쿠폰으로 지급될 스시의 종류가 포함되어있지 않다면 1 증가
    if not sushi_table[c]:
        sushi_table[c] = 1
        n_kinds += 1

    # 기존 정답보다 종류가 더 많을 때 갱신
    if n_kinds > answer:
        answer = n_kinds

print(answer)
