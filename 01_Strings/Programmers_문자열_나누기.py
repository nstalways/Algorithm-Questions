from collections import deque

def solution(s):
    answer = 0
    s = deque(list(s))
    
    while s:
        x = s.popleft()
        answer += 1
        
        cnt_x, cnt_not_x = 1, 0
        for _ in range(len(s)):
            ch = s.popleft()
            
            if x == ch:
                cnt_x += 1
            else:
                cnt_not_x += 1
                
            if cnt_x == cnt_not_x:                
                break
            
            elif not s:
                break
    
    return answer


if __name__ == "__main__":
    print(solution("banana")) # 3
    print(solution("abracadabra")) # 6
    print(solution("aaabbaccccabba")) # 3