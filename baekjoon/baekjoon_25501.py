T = int(input())

string_list = []
for _ in range(T):
    string_list.append(input())

# 힌트 코드 사용
def recursion(s, l, r, cnt=1):
    # 두 번째 조건을 모두 패스하면서 문자열 길이의 중반 이상까지 오면
    # Palindrome 조건을 만족
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt # 대칭인지 판별하는 부분(핵심)
    else:
        cnt += 1
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, cnt=1)

for string in string_list:
    state, cnt = isPalindrome(string)
    print(state, cnt)
