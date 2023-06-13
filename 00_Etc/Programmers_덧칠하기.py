from collections import deque

def solution(n, m, section):
    answer = 0
    section = deque(section)
    
    end = 0
    while section:
        start = section.popleft()
        
        if start <= end:
            continue
        
        end = start + m - 1
        answer += 1
        
    return answer


if __name__ == "__main__":
    print(solution(8, 4, [2, 3, 6])) # 2
    print(solution(5, 4, [1, 3])) # 1
    print(solution(4, 1, [1, 2, 3, 4])) # 4
    