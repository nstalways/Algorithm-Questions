from sys import stdin
from collections import Counter

# 입력부
N = int(stdin.readline().strip())
cards_sanggeun = dict(Counter(stdin.readline().strip().split()))

M = int(stdin.readline().strip())
cards = stdin.readline().strip().split()

# 문제
answer = []
for card in cards:
    try:
        answer.append(str(cards_sanggeun[card]))
    except:
        answer.append('0')

print(' '.join(answer))

# 해설
'''
1. list.append()의 time complexity는 평균적으로 O(1)이다.
Amortized analysis(분활상환기법)와 관련이 있다는데, 뭔지는 정확히 모르겠다.
이해한 바로는, python의 list는 array-based list이기 때문에 배열의 크기를 초과했을 때 push를 하려면
기존 값들을 모두 복사해야한다. 허나 이 복사 과정이 매번 일어나는 것은 아니고, 분활상환기법에 맞춰
특정 조건에서만 복사가 일어나는 것으로 보인다. 따라서 element당 push의 time complexity는 O(1)이지만,
실제로는 O(n)에 가까운 것으로 이해하였다.
Reference)
https://stackoverflow.com/questions/33044883/why-is-the-time-complexity-of-pythons-list-append-method-o1

2. Python에서 string 간의 concatenation은 O(N+M)의 복잡도를 가진다. (str1의 길이: N, str2의 길이: M)
Python의 string은 immutable한 객체이기 때문에, 특정 값을 변경할 수 없다(접근은 가능하다. ex) a = '123', a[0] >>>> '1')
따라서 concat을 하려면 string 자체를 복사해야 하는데, 만약 loop안에서 str1 += str2와 같은
concat을 수행한다면 time complexity가 O(N**2)에 가까울 것이고, 이는 데이터가 많아질수록 느려진다.
이를 방지할 수 있는 메소드가 string.join(sequential_data) 메소드이다.
join()은 sequential_data의 element를 하나씩 가져와서 string을 기준으로 concat하기 때문에,
time complexity가 O(n)이다.
Reference)
https://stackoverflow.com/questions/37133547/time-complexity-of-string-concatenation-in-python

풀이 과정)
처음에 string concat으로 접근했다가 시간 초과가 나서, list를 이용한 뒤 append()하는 방식으로 풀었다.
list.append() 이후 join()을 사용하면 O(N)을 2번 하는 거니깐, 첫 번째 loop에서 concat을 하면 O(n)으로
가능하겠다고 생각했으나 사실 복잡도는 O(N**2)였고, 시간 초과가 발생했다.
문제를 풀고 나서 의문이 생긴 것이, 아는 바로는 python의 list가 array-based list였고, array-based list는
배열의 크기가 모자랄 때 push를 하면 기존 값들을 모두 복사해야하기 때문에 O(N)으로 이해했었다.
그렇다면 loop의 시간복잡도는 O(N**2)일 것이고 시간 초과로 틀려야 했는데, 정답인 점이 의문스러웠다.
그래서 찾아보니, 분할상환기법이라는 생소한 걸 보게 됐고 평균적으로 O(1)이라고 대충 이해할 수 있었다.

'''