from itertools import combinations


def solution(l, alphabets):
    # 자음, 모음 분리
    vowels, consonants = [], []
    for alphabet in alphabets:
        if alphabet in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(alphabet)
        else:
            consonants.append(alphabet)
    
    # 조합 구성
    answer = []
    for num_vowels in range(1, l - 1):
        num_consonants = l - num_vowels

        vowel_cands = list(combinations(vowels, num_vowels))
        conso_cands = list(combinations(consonants, num_consonants))

        for vowel_cand in vowel_cands:
            for conso_cand in conso_cands:
                answer.append(''.join(sorted(list(vowel_cand) + list(conso_cand))))

    answer.sort()
    for idx in range(len(answer)):
        print(answer[idx])
    

if __name__ == "__main__":
    L, C = map(int, input().split())
    alphabets = list(input().split())

    solution(L, alphabets)
    