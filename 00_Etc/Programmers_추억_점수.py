def solution(name, yearning, photo):
    answer = []
    
    score_dict = {name:year for name, year in zip(name, yearning)}
    
    for p in photo:
        score_per_image = 0
        for person in p:
            try:
                score_per_image += score_dict[person]
            except:
                pass
        
        answer.append(score_per_image)    
    
    return answer
