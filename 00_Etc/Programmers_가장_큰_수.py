def solution(numbers):
    # 예외 처리
    if len(numbers) == 1:
        return str(numbers[0])
    
    numbers = [str(n) for n in numbers]
    numbers.sort(reverse=True, key=lambda x: x*4)
    
    if numbers[0] == '0':
        return numbers[0]
    else:
        return ''.join(numbers)


if __name__ == "__main__":
    print(solution([6, 10, 2])) # "6210"
    print(solution([3, 30, 34, 5, 9])) # "9534330"

    a = ['30', '3', '34']
    print(sorted(a))
    print(sorted(a, reverse=True))
    print(sorted(a, key=lambda x: x*4))
    print(sorted(a, reverse=True, key=lambda x: x*4))