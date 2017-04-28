if __name__ == '__main__':
    N = int(input())
    A = [int(a) for a in input().strip().split(' ')]

    sum1, sum2, sum3 = 0, 0, 0
    try:
        i = 0
        while i < N:
            sum1 += A[i]
            sum2 += A[i+1]
            sum3 += A[i+2]

            i += 3
        print(sum1, sum2, sum3)
    except IndexError:
        print(sum1, sum2, sum3)
