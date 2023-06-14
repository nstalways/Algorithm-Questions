def solution(babbling):
    answer = 0
    can_pronounce = ['aya', 'ye', 'woo', 'ma']
    
    for b in babbling:
        b_cp = b
        for p in can_pronounce:
            # 연속발음 예외처리
            if b_cp.replace(p*2, '') != b_cp:
                break
            
            b_cp = b_cp.replace(p, ' ')
        
        b_cp = b_cp.replace(' ', '')
        
        if not b_cp:
            answer += 1
            
    return answer


if __name__ == "__main__":
    print(solution(["aya", "yee", "u", "maa"])) # 1
    print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])) # 2