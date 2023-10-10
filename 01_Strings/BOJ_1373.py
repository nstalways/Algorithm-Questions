import sys

def solution(bin_num):
    print(oct(int(bin_num, 2))[2:])


if __name__ == "__main__":
    bin_num = sys.stdin.readline().strip()

    solution(bin_num)
