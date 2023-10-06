import sys

def solution(words):
    # 대/소문자 구분 X -> 소문자로 통일
    tmp = []
    for pos, word in enumerate(words):
        tmp.append((''.join([ch.lower() for ch in word]), pos))
    
    # 정렬
    tmp.sort()

    # 사전순 맨 앞 단어를 원래 단어 리스트에서 검색
    res = words[tmp[0][-1]]
    
    return res


if __name__ == "__main__":
    input = sys.stdin.readline

    ans = []
    while True:
        n = int(input().strip())
        if n == 0:
            break
        
        words = []
        for _ in range(n):
            words.append(input().strip())

        ans.append(solution(words))
    
    print(*ans, sep='\n')
