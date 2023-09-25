def solution(colors):
    data_sheet = {'black': 0, 'brown': 1, 'red': 2,
                  'orange': 3, 'yellow': 4, 'green': 5,
                  'blue': 6, 'violet': 7, 'grey': 8,'white': 9}

    ans = ''
    for idx, color in enumerate(colors, start=1):
        if idx == len(colors): 
            ans = int(ans) * (10 ** data_sheet[color])
            break

        ans += str(data_sheet[color])

    return ans


if __name__ == "__main__":
    colors = [input() for _ in range(3)]
    print(solution(colors))
        