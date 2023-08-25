def divide(arr):
    size = len(arr)
    delimiter = size // 2
    
    divided = [[] for _ in range(4)]
    for row in arr:
        if len(divided[0]) < delimiter:
            divided[0].append(row[:delimiter])
            divided[1].append(row[delimiter:])
        else:
            divided[2].append(row[:delimiter])
            divided[3].append(row[delimiter:])

    return divided


def can_compress(arr):
    flag = True
    base = arr[0][0]

    for row in arr:
        kinds = list(set(row))

        if base != kinds[0] or len(kinds) == 2:
            flag = False
            break

    return flag


def compress(arr):
    return arr[0][0]


def quad_tree(arr):
    flag = can_compress(arr)

    if flag: # 압축이 가능하면
        return compress(arr)
    
    # 압축이 불가능하면
    divided_arr = divide(arr) # 먼저 4등분
    res = '('

    for div in divided_arr:
        res += str(quad_tree(div))

    res += ')'

    return res
    

if __name__ == "__main__":
    N = int(input())

    img = []
    for _ in range(N):
        img.append([int(x) for x in list(input())])
    
    ans = quad_tree(img)
    print(ans)
