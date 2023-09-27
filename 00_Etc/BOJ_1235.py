import sys

def solution(students, n):
    k = 1
    while True:
        tmp = []
        for student in students:
            tmp.append(student[-k:])
        
        if len(set(tmp)) == n:
            break

        k += 1
    
    print(k)


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    students = []
    for _ in range(N):
        students.append(input().strip())
    
    solution(students, N)
    