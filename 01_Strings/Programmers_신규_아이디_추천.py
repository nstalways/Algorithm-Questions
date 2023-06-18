def check_answer(results, answers):
    for p, a in zip(results, answers):
        if p == a:
            print('True')
        else:
            print('False')


def solution(new_id):
    answer = ''
    
    # step 1
    after_step1 = ''.join([ch.lower() if ch.isalpha() else ch for ch in new_id])
    # print(after_step1)
    
    # step 2
    after_step2 = ''.join([ch for ch in after_step1 if ch.isalpha() or ch.isdigit() or ch in ['-', '_', '.']])
    # print(after_step2)
    
    # step 3    
    while after_step2.find('..') + 1:
        after_step2 = after_step2.replace('..', '.')
    
    after_step3 = after_step2
    # print(after_step3)
    
    # step 4
    after_step4 = list(after_step3)
    if after_step4 and after_step4[0] == '.':
        after_step4 = after_step4[1:]

    if after_step4 and after_step4[-1] == '.':
        after_step4 = after_step4[:-1]
    
    after_step4 = ''.join(after_step4)
    # print(after_step4)
    
    # step 5
    after_step5 = after_step4
    if not after_step5:
        after_step5 = 'a'
        
    # print(after_step5)
    
    # step 6
    after_step6 = after_step5
    if len(after_step5) >= 16:
        after_step6 = after_step5[:15]
        
        if after_step6[-1] == '.':
            after_step6 = after_step6[:-1]
    
    # print(after_step6)
        
    # step 7
    after_step7 = after_step6
    if len(after_step7) <= 2:
        for _ in range(3 - len(after_step7)):
            after_step7 += after_step6[-1]

    return after_step7


if __name__ == "__main__":
    problems = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
    answers = ["bat.y.abcdefghi", "z--", "aaa", "123_.def", "abcdefghijklmn"]

    results = []
    for prob in problems:
        results.append(solution(prob))
    
    check_answer(results, answers)