from collections import Counter


def solution(name):
    data = sorted(Counter(name).items(), key=lambda x: x[0])
    
    odd_cnt = 0
    front, center = [], []
    is_palindrome = True
    for ch, cnt in data:
        if (cnt % 2) != 0:
            odd_cnt += 1
        
        if (len(name) % 2) == 0 and odd_cnt:
            is_palindrome = False
            break
        elif (len(name) % 2) != 0 and odd_cnt > 1:
            is_palindrome = False
            break
        else:
            div, mod = divmod(cnt, 2)
            front.extend([ch] * div)
            
            if mod:
                center.append(ch)
    
    if is_palindrome:
        rear = front[::-1]
        answer = ''.join(front + center + rear)

        print(answer)
    else:
        print("I'm Sorry Hansoo")


if __name__ == "__main__":
    name = input()

    solution(name)
    