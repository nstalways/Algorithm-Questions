import sys

def solution(base8):
    base8to2 = {'0':'000', '1':'001', '2':'010',
                '3':'011', '4':'100', '5':'101',
                '6':'110', '7':'111'}
    
    res = []
    for n in base8:
        res.append(base8to2[n])
    
    ans = ''.join(res)
    ans = ans.lstrip('0')

    if ans:
        print(ans)
    else:
        print('0')

def solution2(base8):
    print(bin(int(base8, 8))[2:])


if __name__ == "__main__":
    base8 = sys.stdin.readline().strip()
    solution(base8)
    solution2(base8)
    