def solution(file_name_list):
    len_file_name = len(file_name_list[0])

    answer = []
    for idx in range(len_file_name):
        prev_ch = ''

        for file_name in file_name_list:
            if not prev_ch:
                prev_ch = file_name[idx]
                continue
                
            if prev_ch != file_name[idx]:
                prev_ch = '?'
                break
        
        answer.append(prev_ch)
        
    print(''.join(answer))


if __name__ == "__main__":
    N = int(input())

    file_name_list = []
    for _ in range(N):
        file_name_list.append(input())
    
    solution(file_name_list)
    