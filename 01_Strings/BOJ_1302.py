import sys

def solution(book_receipts: dict):
    # 사전순 정렬 -> 판매량 순서 정렬 (stable sort이기 때문에 가능)
    order_dict = sorted(book_receipts.items(), key=lambda x: x[0])
    order_cnt = sorted(order_dict, key=lambda x: x[1], reverse=True)

    ans, _ = order_cnt[0]
    print(ans)
    

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    book_receipts = {}
    for _ in range(N):
        book = input().strip()
        if book in book_receipts.keys():
            book_receipts[book] += 1
        else:
            book_receipts[book] = 1
    
    solution(book_receipts)
