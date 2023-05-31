def solution():
    # 입력
    t = int(input())
    balances = []
    coins = [25, 10, 5, 1]

    for _ in range(t):
        balances.append(int(input()))
    
    # 거스름돈 알고리즘
    answer = []
    for balance in balances:
        tmp = []
        curr_val = balance
        for coin in coins:
            tmp.append(str(curr_val // coin))
            curr_val = curr_val % coin
        
        answer.append(' '.join(tmp))

    # 출력
    for line in answer:
        print(line)


if __name__ == "__main__":
    solution()