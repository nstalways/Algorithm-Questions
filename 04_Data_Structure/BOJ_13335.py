import sys
input = sys.stdin.readline

# 입력
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

# 풀이
from collections import deque

trucks = deque(trucks)
on_bridge = deque()

t = 0
while True:
    # 남은 트럭이 없고, 다리 위에도 아무것도 없으면 종료
    if not trucks and not on_bridge:
        print(t)
        break
    
    if not on_bridge:
        if trucks:
            on_bridge.append([trucks.popleft(), 1])

    else:
        if on_bridge[0][1] >= w:
            on_bridge.popleft()
        
        cum_weights = 0
        for i in range(len(on_bridge)):
            cum_weights += on_bridge[i][0]
            on_bridge[i][1] += 1

        if trucks:
            if cum_weights + trucks[0] <= l:
                on_bridge.append([trucks.popleft(), 1])
    
    t += 1
