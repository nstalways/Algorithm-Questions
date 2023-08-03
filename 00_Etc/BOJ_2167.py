import sys


def solution(arr, indexes_list):
    for indexes in indexes_list:
        i, j, x, y = indexes

        answer = 0
        for m in range(i-1, x):
            answer += sum(arr[m][j-1: y])

        print(answer)


if __name__ == "__main__":
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))
    
    K = int(input())

    indexes_list = []
    for _ in range(K):
        indexes_list.append(list(map(int, sys.stdin.readline().split())))

    solution(arr, indexes_list)
    