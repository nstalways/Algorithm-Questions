import sys

# 단어 -> 문자 순서대로 확인
def solution(options):
    shortkey_info = {chr(ch): False for ch in range(ord('a'), ord('z') + 1)}

    for option in options:
        flag = False

        # 1. 단어를 먼저 확인
        for i, word in enumerate(option):
            shortkey = word[0]
            if not shortkey_info[shortkey.lower()]:
                flag = True
                shortkey_info[shortkey.lower()] = flag
                option[i] = f'[{shortkey}]{word[1:]}'
                break
        
        if flag:
            print(' '.join(option))
        else:
            # 2. 알파벳을 확인
            flag = False
            for i, word in enumerate(option):
                alphas = list(word)
                for j in range(1, len(alphas)):
                    shortkey = alphas[j]
                    if not shortkey_info[shortkey.lower()]:
                        flag = True
                        shortkey_info[shortkey.lower()] = flag
                        alphas[j] = f'[{shortkey}]'
                        break
                
                if flag:
                    option[i] = ''.join(alphas)
                    print(' '.join(option))
                    break

                if i == len(option) - 1 and not flag:
                    print(' '.join(option))
                    break


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    options = []
    for _ in range(N):
        options.append(input().split())

    solution(options)
