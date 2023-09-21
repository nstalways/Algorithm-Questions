import sys

def solution(word):
    candidates = []

    word = list(word)

    for pos1 in range(1, len(word)):
        for pos2 in range(pos1 + 1, len(word)):
            word1 = list(word[:pos1])
            word2 = list(word[pos1:pos2])
            word3 = list(word[pos2:])

            word1.reverse()
            word2.reverse()
            word3.reverse()

            candidates.append(''.join(word1 + word2 + word3))

    answer = sorted(candidates)[0] 

    return answer


if __name__ == "__main__":
    word = sys.stdin.readline().strip()

    print(solution(word))
    