def solution(n, lost, reserve):
    answer = 0
    
    students, lost, reserve = set([x for x in range(1, n + 1)]), set(lost), set(reserve)
    exception = lost & reserve # 여벌 체육복을 가져온 학생이 도난당한 경우
    real_reserve, real_lost = (reserve - exception), (lost - exception)
    have = students - real_lost
    
    answer += len(have)
    
    real_lost = list(real_lost)
    for r in real_reserve:
        if (r - 1) in real_lost:
            answer += 1
            real_lost.remove(r - 1)
        elif (r + 1) in real_lost:
            answer += 1
            real_lost.remove(r + 1)
    
    return answer


if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5])) # 5
    print(solution(5, [2, 4], [3])) # 4
    print(solution(3, [3], [1])) # 2
    print(solution(5, [2, 4], [2, 3, 5])) # 5