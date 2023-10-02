import sys

def solution(docs, query):
    docs_cp = docs
    len_query = len(query)

    cnt = 0
    while True:
        can_search = docs_cp.find(query)
        if can_search > -1:
            cnt += 1
            docs_cp = docs_cp[can_search + len_query:]
        else:
            print(cnt)
            break
    

if __name__ == "__main__":
    input = sys.stdin.readline

    docs = input().strip()
    query = input().strip()

    solution(docs, query)
