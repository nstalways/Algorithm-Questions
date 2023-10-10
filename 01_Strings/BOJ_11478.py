import sys

def solution(s):
    substrings = set()
    len_s = len(s)
    
    offset = 1
    while offset <= len_s:
        for start in range(0, len_s - offset + 1):
            substrings.add(s[start:start + offset])

        offset += 1

    print(len(substrings))


if __name__ == "__main__":
    S = sys.stdin.readline().strip()

    solution(S)
