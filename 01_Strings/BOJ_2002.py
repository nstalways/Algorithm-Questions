import sys

def solution(tunnel_in, tunnel_out):
    cnt = 0
    for out_car_num, out_order in tunnel_out.items():
        for in_car_num in tunnel_in:
            # 터널 진입 시 내 앞에 차만 고려
            if out_car_num == in_car_num:
                break
            
            # 터널 진입 시 내 앞에 있던 차가 여전히 앞에 있는지 확인 -> 없으면 추월 확실
            if tunnel_out[in_car_num] > out_order:
                cnt += 1
                break
    
    print(cnt)


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    tunnel_in = []
    for in_order in range(N):
        tunnel_in.append(input().strip())
    
    tunnel_out = {}
    for out_order in range(N):
        tunnel_out[input().strip()] = out_order

    solution(tunnel_in, tunnel_out)
    