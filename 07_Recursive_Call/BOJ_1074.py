def solution(orig_pts, shape, target_pts, cnt=0):
    # base
    if shape == (1, 1):
        return cnt

    orig_r, orig_c = orig_pts

    h, w = shape
    h, w = h // 2, w // 2

    target_r, target_c = target_pts

    # section 1
    if orig_r <= target_r <= orig_r + h - 1 and \
        orig_c <= target_c <= orig_c + w - 1:

        cnt = solution((orig_r, orig_c), (h, w), target_pts, cnt)
    # section 2
    elif orig_r <= target_r <= orig_r + h - 1 and \
        orig_c + w <= target_c <= orig_c + 2 * w - 1:

        cnt += (h * w)
        cnt = solution((orig_r, orig_c + w), (h, w), target_pts, cnt)
    # section 3
    elif orig_r + h <= target_r <= orig_r + 2 * h - 1 and \
        orig_c <= target_c <= orig_c + w - 1:

        cnt += 2 * (h * w)
        cnt = solution((orig_r + h, orig_c), (h, w), target_pts, cnt)
    # section 4
    elif orig_r + h <= target_r <= orig_r + 2 * h - 1 and \
        orig_c + w <= target_c <= orig_c + 2 * w - 1:

        cnt += 3 * (h * w)
        cnt = solution((orig_r + h, orig_c + w), (h, w), target_pts, cnt)

    
    return cnt


if __name__ == "__main__":
    N, r, c = map(int, input().split())

    orig_pts = (0, 0)
    shape = (2**N, 2**N)
    target_pts = (r, c)

    print(solution(orig_pts, shape, target_pts))
    