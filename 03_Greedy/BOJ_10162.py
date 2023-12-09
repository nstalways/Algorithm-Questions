# 입력
T = int(input())

# 풀이
"""
[입력]
- T (sec): 요리해야할 시간 (1 이상 1만 이하)

[출력]
- 주어진 요리시간 T초를 맞추기 위한 최소버튼 조작 방법 구하기

[조건]
- 세 개의 버튼은 각각 일정한 시간이 지정되어 있음.
    - A: 300s, B: 60s, C: 10s
- 버튼을 누른 횟수를 최소로 하면서, 시간의 합이 정확히 T초가 되도록 하는 버튼 별 조작 횟수를 구하라
- 만약 정확히 T초로 만들 수 없다면, -1을 출력한다.

[그리디] 구현
- 버튼을 누른 횟수를 최소로 하기 위해선, 지정된 시간이 큰 버튼을 최대한 많이 누르면 됨.
- 버튼을 누르는 것은, 현재 남은 시간을 지정된 시간으로 나누는 것.
- 현재 버튼에 지정된 시간으로 더 이상 나누어지지 않는다면, 다음 버튼에 지정된 시간으로 나눈다.
- 모든 버튼을 눌렀을 때 나머지가 0이라면, 정확히 T가 만들어지는 것이므로 버튼 별 조작 횟수를 출력
- 나머지가 0이 아니라면, T가 만들어지지 않는 것이므로 -1을 출력
"""
pushCnt_per_buttons = []
setTime_per_buttons = [300, 60, 10]

totally_divided = False
for setTime_per_button in setTime_per_buttons:
    cnt, mod = divmod(T, setTime_per_button)

    pushCnt_per_buttons.append(cnt)
    T = mod

if T:
    print(-1)
else:
    print(*pushCnt_per_buttons)
    