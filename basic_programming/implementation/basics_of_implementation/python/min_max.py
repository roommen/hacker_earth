if __name__ == '__main__':
    N = int(input().strip())
    A = [int(a) for a in input().strip().split(' ')]
    min_, max_ = min(A), max(A)
    unique = 1
    for a in range(min_+1, max_):
        if a not in A:
            print('NO')
            unique = 0
            break
    if unique == 1:
        print('YES')
