import sys

input = sys.stdin.readline().rstrip()
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

if len(input) <= 100:    
    for alphabet in croatia_alphabet:
        input = input.replace(alphabet, '*')
    print(len(input))
else:
    print('최대 100글자의 단어만 입력 가능합니다.')
