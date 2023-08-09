def solution(scores):
    # 총점
    scores = sorted(scores, reverse=True, key=lambda x: x[1])
    print(sum([n for _, n in scores[:5]]))

    # 문제
    probs = sorted(scores[:5], key=lambda x: x[0])
    print(' '.join([str(n+1) for n, _ in probs]))


if __name__ == "__main__":
    scores = []
    for num_problem in range(8):
        scores.append((num_problem, int(input())))

    solution(scores)