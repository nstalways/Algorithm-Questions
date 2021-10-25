N = input()

if 1 <= int(N) <= 100:
    word_list = []
    num_group_word = 0
    
    for _ in range(int(N)):
        word = input()
        word_list.append(word)
        # print(f'alphabet: {alphabet}')

    for i in range(int(N)):
        total_cnt = []
        group_word_list = []
        alphabet = set(word_list[i])
        alphabet = list(alphabet)
        
        for j in range(len(alphabet)):
            cnt = word_list[i].count(alphabet[j])
            total_cnt.append(cnt)
            # print(f'count: {cnt}')

            if cnt > 1:
                if alphabet[j]*cnt in word_list[i]:
                    # print(alphabet[j] * cnt)
                    group_word_list.append('O')
                else:
                    group_word_list.append('X')
            else:
                group_word_list.append('O')

        if 'X' not in group_word_list:
                num_group_word += 1

        
    print(num_group_word)

else:
    print('단어의 개수는 1 이상 100 이하여야 합니다.')