N = int(input())
radius_list = list(map(int, input().split()))
ring1 = radius_list[0]
rings = radius_list[1:]

# 두 숫자 간의 최대공약수를 구해서, 각각을 나눠주자
for ring in rings:
    # 최대공약수 찾기
    gcf = 0
    for i in range(1, ring+1):
        if (ring1 % i == 0) and (ring % i == 0):
            gcf = i
        if i > ring1:
            break
    
    # 각각 나누기
    print(f'{ring1 // gcf}/{ring//gcf}')