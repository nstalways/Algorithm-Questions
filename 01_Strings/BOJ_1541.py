import sys


def solution(line):
    # - 기준으로 분리
    ops = [x.split('+') for x in line.split('-')]
    
    answer = 0
    for i, op in enumerate(ops):
        tmp = sum([int(o) for o in op])
        
        if i == 0:
            answer += tmp
        else:    
            answer -= tmp

    print(answer)


if __name__ == "__main__":
    solution(sys.stdin.readline().strip())
    