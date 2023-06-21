from collections import Counter


def solution(word):
    answer = []
    num_alphabet_dict = dict(Counter(word))

    for ascii_num in range(ord('a'), ord('z') + 1):
        curr_alpha = chr(ascii_num)

        try:
            answer.append(str(num_alphabet_dict[curr_alpha]))
        except:
            answer.append('0')

    print(' '.join(answer))


if __name__ == "__main__":
    S = input()

    solution(S)