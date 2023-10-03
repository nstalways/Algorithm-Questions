import sys

def solution(data):
    # 1. 표 만들기
    dna2idx = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
    dna_tbl = [['A', 'C', 'A', 'G'],
               ['C', 'G', 'T', 'A'],
               ['A', 'T', 'C', 'G'],
               ['G', 'A', 'G', 'T']]
    
    # 2. 해독하기
    data_cp = list(data)
    while len(data_cp) > 1:
        c, r = dna2idx[data_cp.pop()], dna2idx[data_cp.pop()]
        res = dna_tbl[r][c]
        data_cp.append(res)        

    print(data_cp[0])


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    dna = input().strip()
    
    solution(dna)
