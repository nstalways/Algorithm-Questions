new_id = input()

if new_id.islower() and len(new_id) < 50:
    print(new_id + '??!')
else:
    print('아이디는 소문자, 길이는 50자 미만이여야 합니다.')