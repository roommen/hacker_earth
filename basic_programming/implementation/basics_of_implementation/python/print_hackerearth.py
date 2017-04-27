if __name__ == '__main__':
    N = int(input())
    S = str(input())

    count_a, count_e, count_h, count_r = S.count('a'), S.count('e'), S.count('h'), S.count('r')
    count_c, count_k, count_t = S.count('c'), S.count('k'), S.count('t')

    min2x = min(count_a, count_e, count_h, count_r)
    minx = min(count_c, count_k, count_t)

    double_down = min2x // 2

    if double_down >= minx:
        print(minx)
    if double_down < minx:
        print(double_down)
