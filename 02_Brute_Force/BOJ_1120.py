import sys

def solution(a, b):
    len_a, len_b = len(a), len(b)
    offset = len_b - len_a
    ans = float('inf')

    for b_start in range(offset + 1):
        part_of_b = b[b_start:b_start + len_a]
        diff = 0
        for ch_a, ch_b in zip(a, part_of_b):
            if ch_a != ch_b:
                diff += 1
        
        ans = min(ans, diff)
    
    return ans
        

if __name__ == "__main__":
    A, B = sys.stdin.readline().split()

    print(solution(A, B))
