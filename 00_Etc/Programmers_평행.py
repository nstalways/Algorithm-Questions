from itertools import combinations


def solution(dots):
    answer = 0
    c_dots = list(combinations(dots, 2))
    
    for c_dot in c_dots:
        p1, p2 = sorted(c_dot, key=lambda x: (x[0], x[1]))
        p3, p4 = sorted([x for x in dots if x not in c_dot], key=lambda x: (x[0], x[1]))
        
        # line 1
        x1, y1 = p1
        x2, y2 = p2
        
        # line 2
        x3, y3 = p3
        x4, y4 = p4
        
        if (y2 - y1) / (x2 - x1) == (y4 - y3) / (x4 - x3):
            answer += 1
            break
            
        
    return answer


if __name__ == "__main__":
    print(solution([[1, 4], [9, 2], [3, 8], [11, 6]])) # 1
    print(solution([[3, 5], [4, 1], [2, 4], [5, 10]])) # 0